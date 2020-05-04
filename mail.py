from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome()

driver.get('https://mail.ru/')
assert 'Mail.ru' in driver.title


elem = driver.find_element_by_id('mailbox:login')
elem.send_keys('study.ai_172')
elem.send_keys(Keys.RETURN)

time.sleep(1)

elem = driver.find_element_by_id('mailbox:password')
elem.send_keys('NewPassword172')
elem.send_keys(Keys.RETURN)

time.sleep(5)

first_letter = driver.find_element_by_xpath("//div[@class='llc__container']")
first_letter.click()

mails = []

while True:
    result = {}
    time.sleep(5)
    sender = driver.find_element_by_xpath("//div[@class='letter__author']/span[@class='letter-contact']").text
    date = driver.find_element_by_xpath("//div[@class='letter__date']").text
    topic = driver.find_element_by_xpath("//h2[@class='thread__subject thread__subject_pony-mode']").text
    text = driver.find_element_by_class_name("letter-body").text

    result['sender'] = sender
    result['date'] = date
    result['topic'] = topic
    result['text'] = text

    mails.append(result)

    next_letter = driver.find_element_by_class_name("portal-menu-element_next")
    next_letter.click()


driver.quit()


