from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

URL = "https://www.google.co.kr/imghp?hl=ko&ogbl"
ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

find_name = "박효"

import os

model_object_file_path =  find_name
if not os.path.exists(model_object_file_path):
    os.makedirs(model_object_file_path)


driver = webdriver.Chrome()
driver.get(URL)
elem = driver.find_element(By.NAME, "q")
elem.send_keys(find_name)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        try:
            driver.find_element(CSS_SELECTOR, ".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements(CSS_SELECTOR,".rg_i.Q4LuWd")
count = 1

for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element(CSS_SELECTOR, ".n3VNCb.KAlRDb").get_attribute('src')
        urllib.request.urlretrieve(imgUrl, find_name + "/" + find_name + "_" + str(count) + ".jpg")
        print("Image saved: {0}_{1}.jpg".format(find_name, count))
        count += 1
    except:
        pass

driver.close()





