import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@name='confirmation']").click()
a = driver.switch_to.alert
alt_text = a.text
print(alt_text)
time.sleep(3)
# a.dismiss()
a.accept()
# driver.find_element(By.XPATH,"//input[@name='prompt']").click()
# a = driver.switch_to.alert
# atxt=a.text
# print(atxt)
# # driver.switch_to.alert.send_keys("ASDFGH")
# time.sleep(5)
# # a.send_keys("ITC")
# a.dismiss()