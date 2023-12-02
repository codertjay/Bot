"""
This is used to make a post request to update or create transfer
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Find the iframe element

BASE_URL = "https://is.gd/P0jmCL"


class OneXBET:
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
        super(OneXBET, self).__init__()

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



    def get_click_link(self):
        """
        This is used to interact with elements in the iframe
        """
        try:
            # Create a new WebDriver instance for each interaction
            counter = 0
            while True:
                links = ["https://is.gd/Oyjbv8","https://is.gd/P0jmCL","https://is.gd/ty4rLp"]
                for item in links:
                    self.driver.get(item)
                    counter += 1
                    
                    print(counter)
        except Exception as e:
            print("An error occurred:", e)


try:

    bot = OneXBET(teardown=True)
    bot.get_click_link()
    print("Exiting")

except Exception as a:
    print(a)
