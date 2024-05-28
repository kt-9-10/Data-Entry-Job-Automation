from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

FORM_URL = os.environ["FORM_URL"]


class FormController:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(1200, 900)
        self.driver.get(FORM_URL)

    def submit_form(self, addresses, prices, links):
        for i in range(0, len(addresses)):
            address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            sleep(1)
            address_input.send_keys(addresses[i])
            price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            sleep(1)
            price_input.send_keys(prices[i])
            link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            sleep(1)
            link_input.send_keys(links[i])

            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            submit_button.send_keys(Keys.ENTER)
            sleep(1)

            next_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            next_button.send_keys(Keys.ENTER)
            sleep(1)

        self.driver.quit()