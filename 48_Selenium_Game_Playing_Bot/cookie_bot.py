import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
money = 0
addons = driver.find_elements(By.CSS_SELECTOR, value="#store div")
addons_ids = [addon.get_attribute("id") for addon in addons]
print(f"addons_ids = {addons_ids}")


def click_cookie():
    # print(f"cookie click comecou as {time.time()}")
    cookie = driver.find_element(By.ID, value="cookie")
    while not exit_flag.is_set():
        cookie.click()


def get_addon():
    while not exit_flag.is_set():
        # print(f"addon comecou as {time.time()}")
        money = int(driver.find_element(By.ID, value="money").text)
        print(f"money = {money}")

        addon_to_get_index = ""
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        addon_prices = []
        for price_element in all_prices:
            price = price_element.text
            if price != "":
                addon_prices.append(
                    int(price_element.text.split("-")[1].strip().replace(",", ""))
                )

        for index, price in enumerate(addon_prices):
            if money > price:
                addon_to_get_index = index

        if addon_to_get_index != "":
            addon = driver.find_element(By.ID, value=addons_ids[addon_to_get_index])
            if addon != "":
                addon.click()
                # print(f"click comecou as {time.time()}")
                # print("Click")
    # time.sleep(1)


exit_flag = threading.Event()


# print(f"comecou {time.time()}")
click_thread = threading.Thread(target=click_cookie)
get_addon_thread = threading.Thread(target=get_addon)
# print(f"thread criadas as {time.time()}")
click_thread.start()
get_addon_thread.start()

time.sleep(300)
exit_flag.set()

click_thread.join()
get_addon_thread.join()

cookie_per_s = driver.find_element(by=By.ID, value="cps").text
print(f"cookie per s = {cookie_per_s}")

driver.quit()
