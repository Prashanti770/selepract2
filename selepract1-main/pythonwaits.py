import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    # create webdriver object
    driver = webdriver.Edge(executable_path="C:\\edgedriver_win64 (1)\\msedgedriver.exe")

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
   # driver.implicitly_wait(20)

    driver.find_element(By.XPATH,"//input[@id='user-name']").clear()
    driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")

    driver.find_element(By.XPATH,"//input[@id='password']").clear()
    driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce123")
    driver.find_element(By.XPATH,"//input[@id='login-button']").click()
    driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()

except Exception as e:
    print(e)
    driver.close()

    # print("login successfully")


#     driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
#
#     time.sleep(10)
#     driver.find_element(By.XPATH,"//a[@id='about_sidebar_link']").click()
#     driver.back()
#
#     # wait 10 seconds before looking for element
#
#     # element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpackl']")))
#     # element.click()
#
#     driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']").click()
#
#     # actvalue=driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']").get_attribute("name")
#     # print(actvalue)
#
#     actvalue1 = driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-backpack']").text
#     print(actvalue1)
#
#     #driver.find_element(By.LINK_TEXT,"Automated Testing").click()
#
# # except TimeoutException :
# #     print("Timeout, element not found")
# #     driver.close()
# #
# # except NoSuchElementException :
# #
# #     print("Unable to locate element")
# #
# #     driver.close()

# except (NoSuchElementException, TimeoutException, ElementNotInteractableException ) as e:
#
#     print("element not found")
#     driver.close()


# else:
#     if actvalue1 == "REMOVE":
#         assert True
#         print("True")
#     else:
#         assert False
