from copy import Error
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
money = 0


def click_cookie():
    cookie = driver.find_element(By.ID, value="cookie")
    for n in range(0, 300):
        cookie.click()


def get_addon():
    while True:
        money = int(driver.find_element(By.ID, value="money").text)
        print(f"money = {money}")
        addons = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        addon_to_get = ""
        for addon in addons:
            if addon.is_displayed():
                addon_elements = addon.find_element(By.CSS_SELECTOR, value="b")
                price = int(addon_elements.text.split("-")[1].strip().replace(",", ""))
                if money > price:
                    addon_to_get = addon
        # print(addon_to_get)
        try:
            addon_to_get.click()
        except AttributeError:
            print("slip")
        except NoSuchElementException:
            print("no element")
        time.sleep(5)


click_thread = threading.Thread(target=click_cookie)
get_addon_thread = threading.Thread(target=get_addon)

click_thread.start()
get_addon_thread.start()

# driver.quit()
