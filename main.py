import requests 
import selectorlib
import smtplib, ssl
import os
import time
from datetime import datetime
import streamlit as st
import plotly.express as px

URL = "https://programmer100.pythonanywhere.com/"

now = datetime.now()

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "sanjayramesh1425@gmail.com"
    password = "xndz dxrk jnpl bynf"

    receiver = "sanjayramesh1425@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def store(extracted):
    schedule = now.strftime("%Y-%m-%d-%H-%M-%S")
    with open('data.txt', 'a') as file:
        line = f"{schedule},{extracted}\n"
        file.write(line)



if __name__=="__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
        time.sleep(2)