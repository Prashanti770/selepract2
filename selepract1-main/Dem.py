from selenium import webdriver
import time
driver = webdriver.Edge(executable_path=r"C:\\edgedriver_win64 (1)\\msedgedriver.exe")
time.sleep(3)
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
