from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from wordcloud import WordCloud, STOPWORDS
from pymongo import MongoClient
from gridfs import GridFS
from googlesearch import search


# TODO: Add constants

MONGODB_CONNECTION = "mongodb+srv://gyanranjan:gyanranjan@cluster0.c5ytjsz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
CHROMEDRIVER_PATH = "chromedriver_win32\\chromedriver.exe"

def connect_mongodb(database, keyword):
    client = MongoClient(MONGODB_CONNECTION)
    db = client[database]
    coll = db[keyword]
    return coll

def connect_gridfs(database):
    client = MongoClient(MONGODB_CONNECTION)
    db = client[database]
    fs = GridFS(db)
    return fs

def store_images_in_db(database, images):
    fs = connect_gridfs(database)
    coll = connect_mongodb(database, "fs.files")
    for image in images:
        contents = requests.get(image[0]).content
        img_doc = coll.find_one({"filename":str(image[0])})
        if img_doc is not None:
            fs.delete(img_doc["_id"])
        fs.put(contents, filename=str(image[0]))

def addhistory(user, data):
    coll = connect_mongodb("user-history", user)
    now = datetime.now()
    history = {"Date": now.strftime("%d/%m/%Y"), "Time":now.strftime("%H:%M")}
    history.update(data)
    if coll.count_documents(filter={}) >= 10:
        coll.find_one_and_delete({})
    coll.insert_one(history)

def display_wordcloud(wc_words, isLink = False):
    print("Generating Wordcloud...")
    stopwords = set(STOPWORDS)
    wordc = WordCloud(background_color="white", width=700, height=350, stopwords = stopwords)
    wc_words.seek(0)
    
    if isLink:
        wordc.generate(open('crawler/static/crawler/wc_words_link.txt', encoding='utf-8').read())
        wordc.to_file('crawler/static/crawler/wc_img_link.png')
    else:
        wordc.generate(open('crawler/static/crawler/wc_words.txt', encoding='utf-8').read())
        wordc.to_file('crawler/static/crawler/wc_img.png')

    topKeyValuePairs = list(wordc.words_.items())[:5]

    wc_words.flush()
    wc_words.close()

    topFiveWords = []
    for topKeyValuePair in topKeyValuePairs:
        topFiveWords.append(topKeyValuePair[0])
    
    return topFiveWords        

class Google:

    def __init__(self, keyword, depth):
        self.keyword = keyword
        self.depth = depth
        self.visitedcoll = connect_mongodb("googledb", "keywords-visited")
        self.coll = connect_mongodb("googledb", self.keyword)

    def googlecrawl(self):

        visited = False
        for _ in self.visitedcoll.find({"keyword":self.keyword}):
            visited = True

        links = []
        wc_words = open('crawler/static/crawler/wc_words.txt', 'w', encoding='utf-8')

        if visited:
            for x in self.coll.find():
                links.append(x["Link"])
                try:
                    wc_words.write(x["Page content"] + "\n\n")
                except Exception:
                    pass
        
        else:
            
            url = "https://google.com/search?q={}".format('+'.join(self.keyword.split(' ')))
            links_found_on_google = list(search(self.keyword, num=25*(self.depth), stop=25*(self.depth), pause=4.0))
            links = [url] + links_found_on_google

            driver = webdriver.Chrome(CHROMEDRIVER_PATH)

            # TODO: Can try headless webdriver ->
            # chrome_options = Options()
            # chrome_options.add_argument("--headless")
            # driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=chrome_options)

            parent = None
            link_count = 0
            for link in links:
                print(link_count, "->", link)
                try:
                    source = requests.get(link, timeout = 20).text
                    curr_page = BeautifulSoup(source, 'lxml')
                    title = curr_page.find('title').text
                    text = ' '.join(curr_page.text.split())
                    wc_words.write(text + "\n\n")
                    driver.get(link)
                    imgs = list(set([element.get_attribute('src') for element in driver.find_elements_by_tag_name('img')]))
                    images = []
                    for img in imgs:
                        images.append([img, False])
                    store_images_in_db("googledb", images)
                    success = True
                except Exception:
                    success = False
                if success:
                    print("Found")
                    self.coll.insert_one({"Link":link, "Title":title, "Page content":text, "Images": images, "Parent link":parent, "Successfully parsed":success})
                else:
                    print("Not found")
                    self.coll.insert_one({"Link":link, "Parent link":parent, "Successfully parsed":success})
                
                link_count += 1
                if link_count == 1:
                    parent = url
            driver.quit()
            self.visitedcoll.insert_one({"keyword":self.keyword})

        topFiveWords = display_wordcloud(wc_words)
        
        return links, topFiveWords
