import html
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://polygonscan.com/tokens?&sort=24h_volume_usd&order=desc&p="


class Polygon:
    def __init__(self, teardown=True):

        s = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('headless')
        self.teardown = teardown
        # keep chrome open
        self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option(
            "excludeSwitches",
            ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=self.options,
            service=s)
        self.tokens = []
        self.driver.implicitly_wait(50)
        super(Polygon, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def get_details_on_links(self):
        for i in range(1, 13):
            url = f"{BASE_URL}{i}"
            self.driver.get(url)

            tableRows = self.driver.find_elements(by=By.TAG_NAME, value="tr")[1:]
            for tableRow in tableRows:
                try:
                    tdToken = tableRow.find_elements(by=By.TAG_NAME, value="td")[1].find_element(
                        by=By.TAG_NAME, value="a").get_attribute("href")
                    twenty_four_hour_volume = tableRow.find_elements(by=By.TAG_NAME, value="td")[4].text
                    token_holders = tableRow.find_elements(by=By.TAG_NAME, value="td")[-1].find_element(by=By.TAG_NAME, value='div').text

                    print(tdToken)
                    print(twenty_four_hour_volume)
                    print(token_holders)

                    tdToken = tdToken.split("/")[-1]
                    twenty_four_hour_volume = twenty_four_hour_volume.replace("$","").replace(",","")
                    twenty_four_hour_volume = float(twenty_four_hour_volume)

                    token_holders = float(token_holders.replace(",",""))

                    if twenty_four_hour_volume >= 100000 and token_holders >= 999:
                        self.tokens.append(tdToken)
                except Exception as a:
                    print(a)

    def dump_data(self):
        with open("polygon.json", "w") as f:
            json.dump(self.tokens, f, indent=4)
