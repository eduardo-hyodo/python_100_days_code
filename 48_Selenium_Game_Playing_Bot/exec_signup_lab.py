from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_element = driver.find_element(By.NAME, value="fName")
last_name_element = driver.find_element(By.NAME, value="lName")
email_element = driver.find_element(By.NAME, value="email")
sign_up_element = driver.find_element(By.CSS_SELECTOR, value="form button")

first_name_element.send_keys("Teste")
last_name_element.send_keys("teste2")
email_element.send_keys("teste@teste.com")
sign_up_element.click()

driver.quit()
