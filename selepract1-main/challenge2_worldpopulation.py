
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.worldometers.info/world-population/")
time.sleep(5)

#Total Population

# while(True):
#     pop= driver.find_elements(By.XPATH,"//div[@class='maincounter-number']/span")
#     for v in pop:
#         cpop = v.text
#         print("Current World Population: ",cpop)
        # time.sleep(5)


#Today : Births, Deaths and Population Growth

xp_value = "//div[text()='Today']//parent::div//span[@class='rts-counter']"
while(True):
    pop= driver.find_elements(By.XPATH,xp_value)
    for v in pop:
        cpop = v.text
        print("Today Population: ")
        print(cpop)



        ##################################
# bt_xp ="//span[@class='rts-counter' and @rel='births_today']"
# dt_xp ="//span[@class='rts-counter' and @rel='dth1s_today']"
# pgt_xp ="//span[@class='rts-counter' and @rel='absolute_growth']"
# while(True):
#     birth= driver.find_elements(By.XPATH,bt_xp)
#     death= driver.find_elements(By.XPATH,dt_xp)
#     pop_growth = driver.find_elements(By.XPATH,pgt_xp)
#     for v in :
#         cpop = v.text
#         print("Today Population: ")
#         print(cpop)
#

# driver.close()
