import time

import openpyxl
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = "https://www.barracudacentral.org/lookups/lookup-reputation"


class Baruda:
    def __init__(self):
        options = uc.ChromeOptions()
        # options.headless = True
        self.driver = uc.Chrome(use_subprocess=True, options=options)
        self.driver.get(BASE_URL)
        self.driver.maximize_window()
        self.accepted_cookies = False
        # # wait for the element to be clickable
        self.wait = WebDriverWait(self.driver, 10)
        self.json_data = []

        super(Baruda, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def fill_all_ip_address(self):
        """
        this is used to fill all ip address
        :return:
        """
        count = 0
        for item in self.json_data:
            try:
                self.fill_out_first_form(item)
            except:
                print("Error occurred on ", item.get("url"))
                #  move back to the base url
                self.driver.get(BASE_URL)
            count += 1
        print("The count", count)

    def fill_out_first_form(self, item):
        """
        thi is used to fill out form
        :return:
        """
        try:
            # Find the form elements by their CSS selectors
            ip_input = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="lookup_entry"]')
            submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value='input[type="submit"]')

            # Fill out the form fields
            ip_address = item.get("url").split("searchterm=")[1]
            ip_input.clear()
            ip_input.send_keys(ip_address)
            # Submit the form
            submit_button.click()
            time.sleep(5)
            #  fill second form
            print("ip_address", ip_address)
            self.fill_second_form(item)
        except Exception as a:
            print("Error occurred on ", item.get("url"))
            #  move back to the base url
            self.driver.get(BASE_URL)

    def fill_second_form(self, item):
        """
        this is used to fill the second form
        :return:
        """
        element = self.driver.find_elements(by=By.CSS_SELECTOR, value='p[class="failure-message"]')
        if len(element) > 0:
            # click the link
            element[0].find_element(by=By.TAG_NAME, value="a").click()
            time.sleep(2)

            email = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="email"]')
            phone = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="phone"]')
            textarea = self.driver.find_element(by=By.CSS_SELECTOR, value='textarea[name="comments"]')

            submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="submit"]')

            email.send_keys(item.get("email"))
            phone.send_keys(123456789)
            textarea.send_keys(item.get("detail"))

            submit_button.click()
            #  move back to the base url 
            self.driver.get(BASE_URL)

    def convert_excel_to_json(self):
        """
        this is used to create json file
        :return:
        """
        # Load Excel workbook
        workbook = openpyxl.load_workbook('deatlls.xlsx')

        # Select worksheet
        worksheet = workbook['Sheet1']

        # Create list to store rows
        data = []

        # Iterate through rows and append to list
        for row in worksheet.iter_rows(min_row=2, values_only=True):
            data.append({
                'url': row[0],
                'name': row[1],
                'email': row[2],
                'confirm_email': row[3],
                'detail': row[4]
            })

        # Convert list to JSON and print
        self.json_data = data
        print("total number of ip", len(data))
        return True


try:
    bot = Baruda()
    bot.convert_excel_to_json()
    bot.fill_all_ip_address()
    print("Done. \n Exiting .....")
    time.sleep(1000)


except Exception as a:
    print(a)
