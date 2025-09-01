import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FormSubmit:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScmA8zadQp2BDUDvx4mzoW4_lnnztxDnQFmNlPn6_O4MHw_-g/viewform")
        time.sleep(2)

    def post_properties(self, price_list, url_list, address_list):
        for price,url,address in zip(price_list,url_list,address_list):
            price_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            address_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
            url_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            price_input.send_keys(price)
            address_input.send_keys(address)
            url_input.send_keys(url)
            submit_button.click()
            time.sleep(1.5)
            self.new_response()
        driver.quit()

    def new_response(self):
        new_response_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        new_response_button.click()
        time.sleep(1.5)
 
