from seleniumScrape import seleniumScraper
from bs4 import BeautifulSoup

def flipScraper(query:str):
    query = query.replace(' ',"%20")
    url = f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    html = seleniumScraper(url)
    soup = BeautifulSoup(html,'html.parser')
    data = soup.find_all(class_ = 'CGtC98')
    data = data[:5]
    json_list = []
    for div in data:
        json = {
            "Name" : div.find(class_ = 'KzDlHZ').text.strip(),
            "url" : "https://www.flipkart.com"+div['href'],
            "price" : div.find('div', class_='Nx9bqj _4b5DiR').text.strip(),
            "rating" : div.find('div', class_='XQDdHH').text.strip()
        }
        json_list.append(json)
    return json_list
