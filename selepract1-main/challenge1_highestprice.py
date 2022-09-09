# click on Highest price product in a product page -> Add to cart -> verify Remove -> check in cart

import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
user_text = "//input[@id='user-name']"
password_text = "//input[@id='password']"
login_click = "//input[@id='login-button']"
home_logo = "//div[@class='bot_column']"
driver.find_element(By.XPATH,user_text).send_keys("standard_user")
driver.find_element(By.XPATH,password_text).send_keys("secret_sauce")
driver.find_element(By.XPATH,login_click).click()
all_prices = driver.find_elements(By.XPATH,"//div[@class='inventory_item_price']")
# print(all_prices)
prices = []
for p in all_prices:
    value = p.text
    rvalue = float(value.replace("$",""))
    prices.append(rvalue)
print("list of all prices",prices)
max_price=max(prices)
print("list of maximum price",max_price)
path2= "//div[normalize-space()='$"+str(max_price)+"']//following-sibling::button"
driver.find_element(By.XPATH,path2).click()
# time.sleep(15)
# driver.close()

