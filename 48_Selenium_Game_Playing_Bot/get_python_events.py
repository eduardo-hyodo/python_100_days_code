from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.get("https://www.fast.com")
driver.get("https://www.python.org")

event_elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")

events = {}
for index, event in enumerate(event_elements):
    time = event.find_element(By.TAG_NAME, "time")
    event_name = event.find_element(By.TAG_NAME, "a")
    events[index] = {"time": time.text, "name": event_name.text}

print(events)

driver.quit()
