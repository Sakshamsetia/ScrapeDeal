from selenium import webdriver

def seleniumScraper(url):
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.execute_script("return document.documentElement.outerHTML;")
    browser.close()
    return html