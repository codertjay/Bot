"""
This is used to make a post request to update or create transfer
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Find the iframe element

BASE_URL = "https://www.augustachronicle.com"


class AugustAchronicle:
    def __init__(self, teardown=True):
        # Specify the path to the locally installed ChromeDriver binary
        chrome_driver_path = "/home/codertjay/PycharmProjects/Bot/chromedriver_linux64/chromedriver2"  # Change this to the actual path

        # Set up ChromeDriver service using the specified path
        s = Service(chrome_driver_path)

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option("excludeSwitches", ['enable-logging'])

        # Use the specified service and options to create the Chrome WebDriver
        self.driver = webdriver.Chrome(options=self.options, service=s)

        self.detail_links = []
        self.page_detail_links = []
        self.driver.implicitly_wait(50)
        super(AugustAchronicle, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(BASE_URL)

    def clear_browser_data(self):
        self.driver.delete_all_cookies()
        # Clear local and session storage
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")

    def get_page_title(self):
        """
        Get the title of the current page.
        :return: Page title as a string.
        """
        return self.driver.title

    def get_click_bot(self):
        """
        This is used to interact with elements in the iframe
        """
        try:
            self.driver.get(
                "https://www.augustachronicle.com/story/sports/high-school/2023/08/28/top-augusta-high-school-softball-cross-country-and-volleyball-athlete/70619145007/")
            print(self.get_page_title())

            aside_element = self.driver.find_element(by=By.CSS_SELECTOR, value='aside[class="gnt_em gnt_em_pd"]')

            print(aside_element.get_attribute("innerHTML"))

            # Wait for the iframe to load
            iframe = aside_element.find_element(by=By.TAG_NAME,
                                                value='iframe')
            # Switch focus to the iframe
            self.driver.switch_to.frame(iframe)
            print(iframe.get_attribute("innerHTML"))

            print(self.get_page_title())

            while True:
                # Find and interact with elements within the iframe
                radio_button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="57151310"]')
                radio_button.click()

                click_button = self.driver.find_element(By.CSS_SELECTOR, 'button.css-vote-button.pds-vote-button')
                click_button.click()

                return_to_poll = self.driver.find_element(By.CSS_SELECTOR, 'a.pds-return-poll')
                return_to_poll.click()

        except Exception as e:
            print("An error occurred:", e)

    def get_clear_storage(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear();")
        self.driver.execute_script("window.sessionStorage.clear();")

    def get_click_poll(self):
        """
        This is used to interact with elements in the iframe
        """
        try:
            # Create a new WebDriver instance for each interaction

            self.driver.get("https://poll.fm/12689416")

            # Find and interact with elements within the page
            radio_button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="57151310"]')
            radio_button.click()

            click_button = self.driver.find_element(By.CSS_SELECTOR, 'a[id="pd-vote-button12689416"]')
            click_button.click()

            # Close the self.driver after interaction
            self.driver.quit()

        except Exception as e:
            print("An error occurred:", e)


try:
    counter = 0
    while True:
        bot = AugustAchronicle(teardown=True)
        # bot.get_click_bot()
        bot.get_click_poll()
        counter += 1
        print(counter)
        print("Exiting")

except Exception as a:
    print(a)
