from selenium.webdriver.common.by import By

import XLUtils
from selenium import webdriver

driver = webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")
driver.get("https://demo.guru99.com/selenium/newtours/")
driver.maximize_window()

path="C:\Prashanti M\Login1.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    #extract data from each column
    username=XLUtils.readData(path,'Sheet1',r,1)
    password=XLUtils.readData(path,'Sheet1',r,2)

    driver.find_element(by=By.NAME, value="userName").send_keys(username)
    driver.find_element(by=By.NAME, value="password").send_keys(password)

    driver.find_element(by=By.NAME, value="submit").click()

    if driver.title== "Mercury" :
        print("test is passed")
        XLUtils.writeData(path,'Sheet1',r,3,"test passed")
    else:
        print("test failed")
        XLUtils.writeData(path,'Sheet1',r,3,"test failed")

    driver.find_element(by=By.LINK_TEXT, value="Home").click()

driver.close()