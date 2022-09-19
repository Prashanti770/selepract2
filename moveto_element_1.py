from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.mercurytravels.co.in/indian-holidays")
time.sleep(5)
# alllinks = driver.find_elements(By.TAG_NAME,"a")
# for i in alllinks:
#     print(i.text)
add_on = driver.find_element(By.LINK_TEXT,"About Us")
act=ActionChains(driver)
act.move_to_element(add_on).perform()
time.sleep(5)