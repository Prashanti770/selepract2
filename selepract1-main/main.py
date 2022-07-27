from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
time.sleep(3)
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
