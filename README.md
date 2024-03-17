Interpreters
# ACE Hackathon's Problem Statement No. 09
## Project Onion - Tor Crawler

# Overview
Project Onion is a comprehensive tool designed to crawl, classify, and report on Tor websites provided by users. It offers an interactive dashboard with features such as analytics, datasets, reports, and more. This project is built using Django, Mongodb, Python, HTML,  Bootstrap, and includes Figma designs, web architecture, and system designs.
# Features
  - User-specified Tor website crawling
  - Website classification and report generation
  - Interactive analytics dashboard
  - Data export and report generation
  - Responsive and modern UI design
  - Machine Learning Image Detection of Onion Site Content
  - Architectural diagrams and system designs
# Technology Stack
- Backend: Django, Python, Mongodb
- Frontend: HTML, Bootstrap
- Machine learning Model: YOLOv3
- Designs: Figma, Lucidchart

# Installation
Clone the repository and navigate to code\project_onion directory then follow the installation steps:
1. Download requirements:
``` 
pip install -r requirements.txt
```
2. Run Python in terminal and execute following command:
```
import nltk
nltk.download()
```
3. Download YOLOv3 from [here](https://drive.google.com/drive/folders/1dtBYEX4laG9VyXap15Z6HZm2Kdfxt_hG?usp=sharing) and save its files at \YOLOv3\project_onion_yolo.weights

4. Insert Mongodb driver code in \crawler\utlis.py

5. Download and Configure Tor browser for private network with Torcc hash password:
Navigate to the tor.exe directory and run the following command
```
tor.exe --hash-password <yourpassword> | more
``` 
Enter the same <yourpassword> in \crawler\darkweb_crawler.py\

# Usage
##Start the Django backend:
```
python manage.py runserver
```
Access the dashboard at http://127.0.0.1:8000/

# Documentation
Detailed documentation, including setup instructions, architectural diagrams, and system designs, can be found in the Plans directory.
### © Copyright 2024 Interpreters - All rights reserved. 
