import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.costco.com/SiteMapDisplayView"

category_urls = [
    'https://www.costco.com/pretend-play.html', 'https://www.costco.com/electronics-tech-toys.html',
    'https://www.costco.com/toys-outdoor-play.html', 'https://www.costco.com/board-games-puzzles.html',
    'https://www.costco.com/remote-control-vehicles.html', 'https://www.costco.com/plush-toys.html']


class Cosco:
    def __init__(self, teardown=True):

        s = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('headless')
        self.teardown = teardown
        # keep chrome open
        self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option(
            "excludeSwitches",
            ['enable-logging']
        )
        self.driver = webdriver.Chrome(
            options=self.options,
            service=s)
        self.driver.implicitly_wait(50)
        self.category = category_urls
        self.products_url = []
        super(Cosco, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def click_and_scrape_category(self):
        self.driver.get(BASE_URL)
        #
        categorys = self.driver.find_elements(by=By.CSS_SELECTOR, value='a[class="body-copy-link"]')
        for item in categorys:
            self.category.append(item.get_attribute("href"))
        print(categorys)
        return self.category

    def get_category_products(self):
        for item in self.category:
            self.driver.get(item)
            self.get_products_detail_url()

    def get_products_detail_url(self):
        elements = self.driver.find_elements(by=By.CSS_SELECTOR, value='div[class="product-tile-set"]')
        for item in elements:
            detail_url = item.get_attribute("data-pdp-url")
            self.products_url.append(detail_url)
            print("Current product count", len(self.products_url))
            # adding the product detail to the json file
            with open("./cosco_product.json", "w") as f:
                f.write(json.dumps(self.products_url))
        try:
            if self.get_next_page():
                #  if it has next page recall the products url
                self.get_products_detail_url()
        except:
            print("An error occured scraping next page")

    def get_next_page(self):
        try:
            self.driver.find_element(by=By.CSS_SELECTOR, value='li[class="forward"]').click()
            #   get the products in the next pages
            return True
        except:
            print("No next page")
            return False

    def get_products_info(self):
        for item in self.products_url:
            self.driver.get(item)
            image_url = self.driver.find_element(by=By.CSS_SELECTOR,
                                                 value='img[id="initialProductImage"]').get_attribute("src")
            product_name = self.driver.find_element(by=By.CSS_SELECTOR,
                                                    value='h1[automation-id="productName"]').get_attribute(
                "innerHTML").strip()
            product_description = self.driver.find_element(by=By.CSS_SELECTOR,
                                                           value='h1[automation-id="productName"]').get_attribute(
                "innerHTML").strip()


bot = Cosco()
# bot.click_and_scrape_category()
bot.get_category_products()
