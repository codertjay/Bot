# This file will include a class with instance methods
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='div[data-filters-group="class"]'
        )
        star_child_elements = star_filtration_box.find_elements(
            by=By.CSS_SELECTOR,
            value="*"
        )
        for star_value in star_values:
            for star_element in star_child_elements:
                if (
                        str(star_element.get_attribute('innerHTML')).strip()
                        == f'{star_value} stars'):
                    star_element.click()

    def sort_price_lowest_first(self):
        element = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='li[data-id="price"]'
        )
        element.click()
