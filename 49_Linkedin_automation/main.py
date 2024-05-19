import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
)

signin_button = driver.find_element(
    By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]"
)

signin_button.click()

time.sleep(1)
username = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")
username.send_keys("teste@teste.com")
password.send_keys("neveronthecode", Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button")
apply_button.click()

driver.quit()
