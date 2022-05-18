# this file is going to include method that will parse
#  the specific data that we need from each one of the deal boxes
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            by=By.CSS_SELECTOR,
            value='div[data-testid="property-card"]'
        )

    def pull_deal_box_attributes(self):
        collection = [

        ]
        for deal_box in self.deal_boxes:
            # Puling hotel name
            # strip removes white spaces
            hotel_name = deal_box.find_element(
                by=By.CSS_SELECTOR,
                value='div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()

            hotel_price = deal_box.find_element(
                by=By.CSS_SELECTOR,
                value='span[class="fcab3ed991 bd73d13072"]'
            ).get_attribute('innerHTML').strip()
            hotel_score = deal_box.find_element(
                by=By.CSS_SELECTOR,
                value='div[class="b5cd09854e d10a6220b4"]'
            ).get_attribute('innerHTML').strip()

            hotel_image = deal_box.find_element(
                by=By.CSS_SELECTOR,
                value='div[class="b8b0793b0e"]'
            ).get_attribute('src')
            collection.append(
                [hotel_name, hotel_price, hotel_image, hotel_score]
            )
        return collection
