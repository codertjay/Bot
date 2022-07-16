""" anti-bot measures and techniques like JA3, fingerprinting,
Akamai anti-bot, PerimeterX, captcha solving"""

# anti bot stop other bot
# perimeterX also stop bot
# captcha solving
# Load selenium components
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    options=options,
    service=Service(ChromeDriverManager().install())
)
driver.get("http://localhost:3000/")
driver.implicitly_wait(30)
my_element = driver.find_element(by=By.TAG_NAME, value="h1")
my_element.click()
my_second_element = driver.find_element(by=By.TAG_NAME, value='button')
my_second_element.click()

"""
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete'
    )
)
"""

driver.find_element(by=By.ID, value='email').send_keys("mail@gmail.com")
driver.find_element(by=By.ID, value='pass').send_keys("password")
driver.find_element(by=By.ID, value='loginbutton').click()
driver.find_element(by=By.ID, value='back').click()
driver.find_element(
    by=By.XPATH,
    value="//input[@placeholder='Whats on your mine Afenikhena Favour']"
).send_keys('Hello')

driver.find_element(
    by=By.CLASS_NAME,
    value="text-green-400"
).click()
