import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(5)
##################################
# f = driver.find_elements(By.TAG_NAME,"iframe")
# for i in f:
#     print(i.get_attribute("name"))
##########################
# driver.switch_to.frame("packageFrame")
# driver.find_element(By.PARTIAL_LINK_TEXT,"AbstractAnnotations").click()
###########################
driver.switch_to.frame("classFrame")
value=driver.find_element(By.XPATH,"//table[@class='overviewSummary']/tbody/tr[1]").text
print(value)
#############################  #to comeout from frame
driver.switch_to.default_content()
#############################
driver.switch_to.frame("packageFrame")
driver.find_element(By.PARTIAL_LINK_TEXT,"Actions").click()