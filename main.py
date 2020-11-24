from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

insectList = []
url = "https://www.enchantedlearning.com/wordlist/insect.shtml"

browser = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
browser.get(url)


bugNamesrc = browser.find_elements_by_xpath("//div[@class='wordlist-item']")
googleSearch = browser.find_element_by_xpath("//input[@name = 'q']")

wikiSearch = browser.find_element_by_xpath("//input[@name = 'search']")
wikiSearchButton = browser.find_element_by_xpath("//input[@type = 'submit']")
# use '' instead of "" for the class = 'wordlist'
# need to get value from the web object
# without .text, type(insect) = <class 'selenium.webdriver.remote.webelement.WebElement'>

for insect in bugNamesrc:
    insectList.append(insect.text)

for crawly in insectList:
    browser.get("https://www.wikipedia.org/")
    wikiSearch.send_keys(crawly)
    sleep(5)
    wikiSearchButton.click()


"""
class insectNameBot:
    def __init__(self):
        bugName = browser.find_elements_by_class_name("wordlist-item")
        print bugName

"""