from seleniumScrape import seleniumScraper
from bs4 import BeautifulSoup

def amazonScrapper(query:str)->list:
    query = query.replace(' ','+')
    url = f"https://www.amazon.in/s?k={query}&crid=U35IZFHVL6RJ&sprefix=laptops%2Caps%2C449&ref=nb_sb_noss_1"
    html = seleniumScraper(url)
    soup = BeautifulSoup(html,'html.parser')
    Row = soup.find_all(class_ = 'puisg-row')
    impRow = soup.find_all(class_ = 'puis-desktop-list-row')
    data = [d for d in Row if "Sponsored" not in d.get_text(strip=True) and d.get_text(strip=True) != "" and d not in impRow]
    data = data[:5]
    json_list = []
    for div in data:
        json = {
            "Name" : div.find('h2',class_='a-size-medium').find('span').text.strip(),
            "url" : "https://www.amazon.in" + div.find('h2',class_='a-size-medium').find_parent('a')["href"],
            "price" : '₹'+div.find('span',class_='a-price-whole').text.strip(),
            "rating" : div.find('span', class_='a-icon-alt').text.split()[0]
        }
        json_list.append(json)
    return json_list