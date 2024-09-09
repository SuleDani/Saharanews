import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('sahara_news.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        title TEXT,
        article_url TEXT,
        image_url TEXT
    )
''')

url = "https://saharareporters.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    for data in soup.find_all('div', {'class': 'card-content'}):
        title = data.find('h2')
        if title:
            print(title.text.strip())

        url = data.find('a')
        if url:
            link = url.get('href')
            print(link)
        
        image = data.find('img')
        if image:
            img = image.get('src')
            print(img)

        print("\n")



conn = sqlite3.connect('sahara_news.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        title TEXT,
        article_url TEXT,
        image_url TEXT
    )
''')


url = "https://saharareporters.com"
response = requests.get(url)


if response.status_code == 200:
    print("URL found")
else:
    print(f'Error: {response.status_code}')
    exit()


soup = BeautifulSoup(response.text, 'html.parser')


for data in soup.find_all('div', {'class': 'card-content'}):
    
    title = data.find('h2')
    if title:
        title_text = title.text.strip()
        print(f"Title: {title_text}")
    else:
        title_text = None

  
    url_tag = data.find('a')
    if url_tag:
        article_link = url_tag.get('href')
        if not article_link.startswith('http'):
            article_link = url + article_link
        print(f"Article URL: {article_link}")
    else:
        article_link = None

   
    image_tag = data.find('img')
    if image_tag:
        img_url = image_tag.get('src')
        if not img_url.startswith('http'):
            img_url = url + img_url
        print(f"Image URL: {img_url}")
    else:
        img_url = None

    
    cursor.execute('''
        INSERT INTO articles (title, article_url, image_url)
        VALUES (?, ?, ?)
    ''', (title_text, article_link, img_url))

    
    conn.commit()

    print("\n---\n")


conn.close()