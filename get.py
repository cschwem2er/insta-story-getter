#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.common.exceptions import SessionNotCreatedException

driver = webdriver.Chrome(executable_path='drivers/chromedriver')

driver.get('https://instagram.com/missiomusic')

elem = driver.find_element_by_class_name("vi798")
elem2 = elem.find_elements_by_xpath("//li[@class='Ckrof']")
#elem3 = elem2.find_elements_by_xpath("")

for item in elem2:
    print(item.get_attribute('outerHTML'))
    input()