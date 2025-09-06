import requests
from fake_useragent import UserAgent
import time
import random
import selenium

def scrape(url:str,query:str="")->str:
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
    html = session.get(url+query.replace(' ','+'),headers=header)
    html.encoding = "utf-8"
    return html.text
