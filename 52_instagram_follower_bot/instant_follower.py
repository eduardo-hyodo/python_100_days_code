import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
# PYTHONPATH=$PWD/../
from gen_data import Data


# PYTHONPATH=$PWD/../
# from gen_data import Data
class InstantFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://instagram.com")
        access_data = Data().get()["app"]
        instagram_secret = access_data[3]["api_key"]

        time.sleep(4)
        signin_button = self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input"
        )
        signin_button.send_keys("hyodo.developer@gmail.com")

        password_text = self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input"
        )
        password_text.send_keys(instagram_secret)

        time.sleep(2)
        login_button = self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]"
                )
        login_button.click()
        time.sleep(5)
        # self.driver.quit()

    def find_following(self):
        search_button = self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a"
               ) 
        search_button.click()
    
        time.sleep(1)
        search_input =  self.driver.find_element(
            By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/input"
                )
        search_input.send_keys("sheiti.hyodo")

        time.sleep(1)
        person_of_interisting = self.driver.find_element(
                By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/a"
                )
        person_of_interisting.click()

        time.sleep(3.5)
        following_button = self.driver.find_element(
                By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/header/section[3]/ul/li[3]/div/a/span"
                )
        following_button.click()
        time.sleep(5)
        return self
    
    def follow(self):
        print("teste")
