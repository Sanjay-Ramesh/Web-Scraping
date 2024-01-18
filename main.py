import requests 
import selectorlib
import time
from datetime import datetime
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

now = datetime.now()

Connection  = sqlite3.connect("datas.db")


def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def store(extracted):
    date = now.strftime("%Y-%m-%d-%H-%M-%S")
    cursor = Connection.cursor()
    cursor.execute("INSERT INTO events VALUES (?, ?)", (date, extracted))
    Connection.commit()


if __name__=="__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)