from crawler.utils import connect_mongodb

def get_images(database, collection):
    if database is None or collection is None:
        return False
    links_images = []
    coll = connect_mongodb(database, collection)
    for x in coll.find():
        # Check if the 'Images' key exists in the document
        if 'Images' in x:
            links_images.append([x["Link"], x["Images"]])
    coll_fs_files = connect_mongodb(database, "fs.files")
    return coll, links_images, coll_fs_files

def delete_gridfs_image(coll, fs, filename):
    img_doc = coll.find_one({"filename":filename})
    if img_doc is not None:
        fs.delete(img_doc["_id"])
    else:
        print(f"Document with filename '{filename}' not found.")


def get_text(database, collection):
    if database is None or collection is None:
        return False
    links_texts = []
    coll = connect_mongodb(database, collection)
    for x in coll.find():
        try:
            # Check if the 'Page content' key exists in the document
            if 'Page content' in x:
                links_texts.append([x["Link"], x["Page content"]])
        except Exception:
            pass
    return coll, links_texts