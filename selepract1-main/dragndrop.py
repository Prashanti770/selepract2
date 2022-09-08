from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(5)
# driver.switch_to.frame("demo-frame")
driver.switch_to.frame(0)
src = driver.find_element(By.XPATH,"//div[@id='draggable']")
dest = driver.find_element(By.XPATH,"//div[@id='droppable']")

act=ActionChains(driver)
act.drag_and_drop(src,dest).perform()
time.sleep(5)
