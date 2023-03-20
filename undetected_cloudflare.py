import time

import openpyxl
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import pickle

BASE_URL = "https://check.spamhaus.org/"


class AutomateProtection:
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

        super(AutomateProtection, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def land_first_page(self):
        self.driver.get(BASE_URL)

    def add_cookies(self):
        # add cookies
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def save_cookies(self):
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def switch_to_cloudflare(self):
        # switch to the Cloudflare iframe
        iframe = self.driver.find_element(By.CSS_SELECTOR, 'iframe[src*="cloudflare"]')
        self.driver.switch_to.frame(iframe)

        # locate the "verify you are human" button inside the iframe using XPath
        button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'label.ctp-checkbox-label input[type="checkbox"]')))

        # click the button
        button.click()
        print("Clicked the 'verify you are human' button in Cloudflare iframe")

        # switch back to the main frame
        self.driver.switch_to.default_content()
        print("By passed")

    def bypass_cloudflare(self):
        """
        this is used to bypass the cloud flare if it shows the button
        :return:
        """
        try:
            try:
                #  check if we are on cloud flare if not it shows no such element
                if self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2#challenge-running'))):
                    print("Still on cloud flare")
                    self.switch_to_cloudflare()
            except TimeoutException:
                print("Cloud flare bypassed")
                return True
        except Exception as e:
            print(f"Bypassing Cloudflare error")
            time.sleep(2)
            self.bypass_cloudflare()

    def accept_cookies(self):
        try:
            # wait for the cookie bar to appear and become clickable
            cookie_bar = self.wait.until(EC.element_to_be_clickable((By.ID, "cookie-bar")))

            # click the "I Understand" button
            i_understand = cookie_bar.find_element(By.CLASS_NAME, "cb-enable")
            i_understand.click()
            #  accepted the cookie
            self.accepted_cookies = True
        except Exception as a:
            print("Error accepting cookies")
            if self.wait.until(EC.invisibility_of_element_located((By.ID, "cookie-bar"))):
                return True
            self.accept_cookies()

    def next_step(self, item):
        """
        this moves to the next step
        :return:
        """
        # bypass cloud flare if exists
        self.driver.get(item.get("url"))

        # wait till the cookies is not available
        self.wait.until(EC.invisibility_of_element_located((By.ID, "cookie-bar")))

        try:
            # if it is listed the get by css selector will fail
            element_hide_details = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.accordion.open-close-blocklist.open")))
            # click the element
            element_hide_details.click()
            print("Open according")
            time.sleep(5)
            element_input = self.driver.find_element(by=By.CSS_SELECTOR, value='span[class="checkmark"]')
            # click the element
            element_input.click()
            print("clicked the checkbox")

            # find and click the next element
            element_next = self.driver.find_element(by=By.CSS_SELECTOR, value='input[aria-label="Next Steps"]')
            # click the element
            element_next.click()
            print("CLick the next step")

            # fill the forms
            self.fill_out_form(item)
        except:
            print("Not listed")

    def fill_out_form(self, item):
        """
        thi is used to fill out form
        :return:
        """
        form = self.driver.find_element(by=By.CSS_SELECTOR, value='form')
        # Find the form elements by their CSS selectors
        name_input = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="fullName"]')
        email_input = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="email"]')
        confirm_email_input = self.driver.find_element(by=By.CSS_SELECTOR, value='input[name="emailConfirmation"]')
        message_input = self.driver.find_element(by=By.CSS_SELECTOR, value='textarea[name="issue"]')
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value='input[type="submit"]')

        # Fill out the form fields
        name_input.send_keys(item.get("name"))
        time.sleep(2)
        email_input.send_keys(item.get("email"))
        time.sleep(2)
        confirm_email_input.send_keys(item.get("confirm_email"))
        time.sleep(2)
        message_input.send_keys(item.get("detail"))

        # Submit the form
        actions = ActionChains(self.driver)
        actions.move_to_element(submit_button).perform()
        time.sleep(2)
        # Click the submit button

        submit_button.click()
        time.sleep(5)

    def fix_all_ip_address(self):
        """this is used to fix all ip by looping through the json"""
        for item in self.json_data:
            # move to next step
            try:
                self.next_step(item)
            except Exception as a:
                print("error on ", item.get('url'))

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
        return True


try:
    bot = AutomateProtection()
    bot.convert_excel_to_json()
    bot.land_first_page()
    bot.bypass_cloudflare()
    bot.accept_cookies()
    bot.fix_all_ip_address()
    print("Done. \n Exiting .....")
    time.sleep(1000)


except Exception as a:
    print(a)
