import math
import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
path = "//div[@id='sidebar']//ul//li/a"
sidebar = driver.find_elements(By.XPATH,path)
len_all = len(sidebar)
print("length of value",len_all)
value = []
for p in range(1,len_all):
    random_value = int(math.floor((random.random()) * len_all))
    print(random_value)
    # rl = driver.find_element(By.XPATH,path+"["+str(random_value)+"]")
    # txt = rl.text
    # print(txt)

    # e = sidebar.get(random_value)
    # txt = e.text
    # print(txt)
    # value.append(random_value)
    rl = sidebar[random_value]
    txt=rl.text
    print(txt)
    rl.click()
    url = driver.current_url
    print("Current link url is  : ",url)

    driver.back()
    time.sleep(5)
# print("length of rando values:",len(value))

