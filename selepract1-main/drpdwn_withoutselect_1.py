from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(5)
drpdwn = driver.find_element(By.XPATH,"//input[@id='justAnInputBox1']")
drpdwn.click()
time.sleep(5)
# values = driver.find_elements(By.XPATH,"//div[@id='comboTree954062DropDownContainer']/ul/li//span/input")
# print("valuesss")
# drpdwn1=driver.find_element(By.XPATH,"//div[@id='comboTree954062DropDownContainer']")
values = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
# print(values)
print("length of values",len(values))

for i in values:
    opt_txt = i.text
    # if opt_txt is not None:
    if opt_txt !="":
        i.click()
        print(opt_txt)
        # continue
        # break

