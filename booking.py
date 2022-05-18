from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from booking_filtrations import BookingFiltration
from booking_report import BookingReport
from prettytable import PrettyTable
BASE_URL = "https://www.booking.com"


class Booking:
    def __init__(self, teardown=True):
        s = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.teardown = teardown
        self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option(
            "excludeSwitches",
            ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=self.options,
            service=s)
        self.driver.implicitly_wait(15)
        super(Booking, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="button[data-tooltip-text='Choose your currency']"
        )
        currency_element.click()
        selected_currency_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=f"a[data-modal-header-async-url-param*='selected_currency={currency}']"
        )
        selected_currency_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.driver.find_element(
            by=By.ID,
            value='ss'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_place_to_go = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value="li[data-i='0'"
        )
        first_place_to_go.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=f"td[data-date='{check_in_date}'"
        )
        check_in_element.click()

        check_out_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=f"td[data-date='{check_out_date}'"
        )
        check_out_element.click()

    def select_adults(self, count=2):
        selection_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=f'label[id="xp__guests__toggle"]'
        )
        selection_element.click()
        while True:
            decrease_adults_element = self.driver.find_element(
                by=By.CSS_SELECTOR,
                value=f'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            adults_value_element = self.driver.find_element(
                by=By.ID,
                value=f'group_adults'
            )
            # should give back the adult count
            adults_value = adults_value_element.get_attribute('value')
            if int(adults_value) == 1:
                break
        increase_button_element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='button[aria-label="Increase number of Adults"]'
        )
        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='button[type="submit"]'
        ).click()

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self.driver)
        filtration.apply_star_rating(3, 4, 5)
        filtration.sort_price_lowest_first()

    def refresh(self):
        self.driver.refresh()

    def report_results(self):
        hotel_boxes = self.driver.find_element(
            by=By.CLASS_NAME,
            value='dcf496a7b9'
        )
        report = BookingReport(hotel_boxes)
        table = PrettyTable(
          field_names=['Hotel Name', 'Hotel Price', 'image','Hotel Score']
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)


