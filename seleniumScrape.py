from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def seleniumScraper(url):
    options = Options()
    options.add_argument("--headless")        # run in background
    options.add_argument("--disable-gpu")     # recommended
    options.add_argument("--no-sandbox")      # for Linux
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)

    browser.get(url)
    html = browser.page_source
    browser.close()
    return html