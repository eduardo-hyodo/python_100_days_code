from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

print(article_count.text)

# article_count.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

driver.quit()
