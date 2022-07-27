import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# create webdriver object
driver = webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//input[@id='user-name']").clear()
driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")

driver.find_element(By.XPATH,"//input[@id='password']").clear()
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()

print("login successfully")

# time.sleep(10)
driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
driver.find_element(By.XPATH,"//a[@id='about_sidebar_link']").click()
driver.back()
driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()

# actvalue=driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']").get_attribute("name")
# print(actvalue)

actvalue1 = driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']").text
print(actvalue1)

#driver.find_element(By.LINK_TEXT,"Automated Testing").click()



driver.close()
