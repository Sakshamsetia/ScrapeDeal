from scrapper import scrape
from seleniumScrape import seleniumScraper
from bs4 import BeautifulSoup

TheHindu = {
    "India":"https://www.thehindu.com/news/national/",
    "World":"https://www.thehindu.com/news/international/",
    "Business":"https://www.thehindu.com/business/",
    "Sport":"https://www.thehindu.com/sport/"
}
def newsScrapper(topic:str = "India"):
    url = TheHindu[topic]
    html = seleniumScraper(url)
    soup = BeautifulSoup(html,"html.parser")
    heads = soup.find_all("h3",class_ = "title")
    heads = heads[:12]
    json_dict = []
    for head in heads:
        json = {
            "title":head.get_text(strip=True),
            "link":head.a["href"],
            "topic":topic
        }
        json_dict.append(json)
    return json_dict