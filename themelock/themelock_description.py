import asyncio
import json
from asyncio import tasks

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ThemelockDescription:
    def __init__(self, teardown=True):

        s = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.teardown = teardown
        # keep chrome open
        self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option(
            "excludeSwitches",
            ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=self.options,
            service=s)
        self.driver.implicitly_wait(50)
        self.collection = []
        super(ThemelockDescription, self).__init__()

    def __enter__(self):
        self.driver.get()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def get_description_and_quote(self, url):
        self.driver.get(url)
        description = await self.driver.find_element(
            by=By.CLASS_NAME, value='descripton'
        ).get_attribute('innerHTML').strip()
        return description

    def append_to_collection(self):
        with open('themelock.json', 'r') as data_file:
            data = json.load(data_file)

            for item in data:
                print(item)
                item['description'] = await self.get_description_and_quote(item['link'])

        with open('themelock.json', 'w') as f:
            f.write(f"{data}")


bot = ThemelockDescription()
bot.append_to_collection()
