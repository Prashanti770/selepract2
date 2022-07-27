import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import XLUtils
from selenium import webdriver

driver = webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")
# time.sleep(5)
driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()



path="C:\Prashanti M\Login2.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1): #starts from 2 row
    #extract data from each column
    username=XLUtils.readData(path,'Sheet1',r,1)
    password=XLUtils.readData(path,'Sheet1',r,2)
    # time.sleep(5)
    driver.find_element(By.XPATH, value="//span[@class='ico-caret sprite-image']").click()
    # time.sleep(2)
        # wait 10 seconds before looking for element
    element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='ico-logino']"))
        )
    element.click()


    # driver.find_element(by=By.XPATH, value="//a[@class='ico-login']").click()
    driver.find_element(by=By.NAME, value="Username").clear()

    driver.find_element(by=By.NAME, value="Username").send_keys(username)
    driver.find_element(by=By.NAME, value="Password").clear()
    driver.find_element(by=By.NAME, value="Password").send_keys(password)

    driver.find_element(by=By.XPATH, value="//input[@class='btn blue-button' and @type='submit']").click()

    if driver.title== "Free and open-source eCommerce platform. ASP.NET based shopping cart. - nopCommerce" :
        print("test is passed")
        XLUtils.writeData(path,'Sheet1',r,3,"test passed")
        driver.find_element(by=By.XPATH, value="//span[@class='ico-caret sprite-image']").click()
        driver.find_element(by=By.XPATH, value="//a[@class='ico-logout']").click()
    else:
        print("test failed")
        XLUtils.writeData(path,'Sheet1',r,3,"test failed")
    # time.sleep(5)

    #driver.find_element(by=By.XPATH, value="//a[@class='desktop-logo']").click()
    driver.refresh()



driver.close()