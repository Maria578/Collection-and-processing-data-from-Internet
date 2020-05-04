from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome()

driver.get('https://mvideo.ru/')
assert 'М.Видео' in driver.title

time.sleep(5)

products_info = []

hits = driver.find_element_by_xpath("//body[@class='home']/div[@class='wrapper']/div[@class='page-content']/"
                                    "div[@class='main-holder sel-main-holder']/div[10]/div[1]/div[2]")

next_page = hits.find_element_by_class_name("next-btn sel-hits-button-next")

while True:
    if next_page:
        next_page.click()
        time.sleep(5)
    else:
        break


products = hits.find_element_by_xpath(".//a[contains(@class, sel-product-tile-title)]")
for product in products:
    result = {}
    info = product.get_attribute("data-product-info")
    result['info'] = info

    products_info.append(result)

driver.quit()

