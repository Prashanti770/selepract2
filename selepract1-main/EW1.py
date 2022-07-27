# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create webdriver object
driver = webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")

# get geeksforgeeks.org
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.XPATH, value="//input[@id='txtUsername']").clear()

element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "txtUsernamee")))
element.send_keys("Admin")




#driver.find_element(by=By.XPATH, value="//input[@id='txtUsername']").send_keys("Admin")

driver.find_element(By.XPATH, value="//input[@id='txtPassword']").clear()

driver.find_element(by=By.XPATH, value="//input[@id='txtPassword']").send_keys("admin123")

driver.find_element(By.ID, value="btnLogin").click()

print("login successfull")

# get element after explicitly waiting for 10 seconds
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.LINK_TEXT, "Courses"))
# )

# click the element
# element.click()



driver.close()
