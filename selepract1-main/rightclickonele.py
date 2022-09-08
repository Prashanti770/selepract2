from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
# driver.maximize_window()
# time.sleep(5)
rightbtn = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
editbtn = driver.find_element(By.XPATH,"//li[@class='context-menu-item context-menu-icon context-menu-icon-edit']")

act=ActionChains(driver)
act.context_click(rightbtn).perform()
editbtn.click()
time.sleep(5)
