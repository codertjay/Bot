"""
This is used to make a post request to update or create transfer
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# Find the iframe element
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.augustachronicle.com"


class AugustAchronicle:
    def __init__(self, teardown=True):
        # Specify the path to the locally installed ChromeDriver binary
        chrome_driver_path = "/home/codertjay/PycharmProjects/Bot/chromedriver_linux64/chromedriver"  # Change this to the actual path

        # Set up ChromeDriver service using the specified path
        s = Service(chrome_driver_path)

        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('headless')
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

    def check_if_iframe_exists(self):
        try:
            self.get_click_bot()
        except:
            return self.get_click_bot()

    def get_click_bot(self):
        """
        This is used to interact with elements in the iframe
        """
        try:

            self.driver.get(
                "https://www.augustachronicle.com/story/sports/high-school/2023/08/28/top-augusta-high-school-softball-cross-country-and-volleyball-athlete/70619145007/")
            print(self.get_page_title())
            try:
                self.driver.find_element(by=By.CSS_SELECTOR,value='button[class="gnt_em_vp_db"]').click()
            except:
                pass

            aside_element = self.driver.find_element(by=By.CSS_SELECTOR, value='aside[class="gnt_em gnt_em_pd"]')
            action = ActionChains(self.driver)
            action.move_to_element(aside_element).perform()
            print(aside_element.get_attribute("innerHTML"))

            # Wait for the iframe to load
            iframe = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
            )
            # Switch focus to the iframe
            self.driver.switch_to.frame(iframe)

            while True:
                try:

                    # Find and interact with elements within the iframe
                    # Find and interact with elements within the page
                    # Wait until the radio button is clickable
                    radio_button = self.driver.find_element(By.CSS_SELECTOR, 'input[value="57151310"]')
                    radio_button.click()

                    click_button = self.driver.find_element(By.CSS_SELECTOR, 'button[id="pd-vote-button12689416"]')
                    click_button.click()

                    return_to_poll = self.driver.find_element(By.CSS_SELECTOR, 'a[class="pds-return-poll"]')
                    return_to_poll.click()
                    print("clicked")
                except Exception as a:
                    print("refreshing ", a)
                    return self.get_click_bot()

        except Exception as e:
            print("An error occurred:", e)


try:
    bot = AugustAchronicle(teardown=True)
    bot.get_click_bot()
    print("Exiting")

except Exception as a:
    print(a)
