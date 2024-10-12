import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# PYTHONPATH=$PWD/../
from gen_data import Data


class InternetSpeedTwitterBot:
    """Models the bot to connect to the internet provider"""

    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_speed(self):
        self.driver.get("https://fast.com")
        time.sleep(10)
        speed_element = self.driver.find_element(By.ID, value="speed-value")

        self.speed = speed_element.text
        # self.driver.quit()

        return self.speed

    def tweet_at_provider(self, internet_speed):
        self.driver.get("https://x.com/login")

        time.sleep(5)
        signin_button = self.driver.find_element(
            By.XPATH, value="//span[text()='Next']"
        )

        username = self.driver.find_element(
            By.XPATH,
            value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input",
        )
        username.send_keys("hyodo.devstudy@gmail.com")
        signin_button.click()

        time.sleep(5)
        user = self.driver.find_element(
            By.XPATH,
            value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input",
        )

        user.send_keys("Devstudyhyodo")
        nextusername = self.driver.find_element(
            By.XPATH,
            value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div",
        )
        nextusername.click()

        time.sleep(5)
        password = self.driver.find_element(
            By.XPATH,
            value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input",
        )
        access_data = Data().get()["app"][3]["secret"]
        password.send_keys(f"{access_data}", Keys.ENTER)

        time.sleep(5)
        tweet_element = self.driver.find_element(
            By.CLASS_NAME, value="DraftEditor-root"
        )
        tweet_element.click()

        time.sleep(2)
        element = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "public-DraftEditorPlaceholder-root")
            )
        )
        ActionChains(self.driver).move_to_element(element).send_keys(
            f"Internet Provider I hired a 200mb byt I got {internet_speed}"
        ).perform()

        post_button = self.driver.find_element(
            By.XPATH,
            value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span",
        )

        post_button.click()
        # time.sleep(230)
        self.driver.quit()
