import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import random

amazon_url = "https://www.amazon.in/s?k="
flipkart_url = "https://www.flipkart.com/search?q="



def scrape(query:str,url:str)->str:
    ACCEPT_LANGS = [
    "en-US,en;q=0.9",
    "en-GB,en;q=0.8",
    "en;q=0.7",
    "fr-FR,fr;q=0.9,en;q=0.7",
]
    session = requests.Session()
    header = {
        "User-Agent":UserAgent().random,
        "Accept-Language":random.choice(ACCEPT_LANGS),
        "Referer": "https://www.google.com/",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding":"gzip, deflate, br, zstd",
        "Connection":"keep-alive"
    }
    time.sleep(random.uniform(1,4))
    html = session.get(url+query.replace(' ','+'),headers=header).text
    return html    
# Trying Scrape Websites {
# a = scrape("Laptops",amazon_url)
# with open("web.html","w",encoding="utf-8") as f:
#     f.write(a)
# a = scrape("Laptops",flipkart_url)
# with open("web2.html","w",encoding="utf-8") as f:
#      f.write(a)}
