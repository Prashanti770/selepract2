
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.worldometers.info/world-population/")
time.sleep(5)
pop= driver.find_element(By.XPATH,"//div[@class='maincounter-number']")
cpop = pop.text
print("Current World Population: ",cpop)
time.sleep(5)
#Today : Births, Deaths and Population Growth


driver.close()
