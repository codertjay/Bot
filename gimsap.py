from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://gimsap.ca/"

collection = [{'title': 'Snacks', 'link': 'https://gimsap.ca/collections/dry-food',
               'image': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Mock-Up-MrJ-YELLOW70g_300x300.jpg?v=1603115269'},
              {'title': 'Oils &amp; Spices', 'link': 'https://gimsap.ca/collections/oils-spices',
               'image': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/collections/iu-35_300x300.png?v=1606144271'},
              {'title': 'Grains', 'link': 'https://gimsap.ca/collections/frontpage',
               'image': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/collections/iu-7_300x300.jpg?v=1606149125'},
              {'title': 'Frozen Meats Fish &amp; Poultry',
               'link': 'https://gimsap.ca/collections/frozen-meats-fish-poultry',
               'image': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/collections/png-transparent-raw-foodism-lamb-and-mutton-meat-chop-loin-chop-meat-food-beef-cooking_300x300.png?v=1606145502'},
              {'title': 'Frozen Vegetables', 'link': 'https://gimsap.ca/collections/frozen-vegetables',
               'image': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/collections/iu-44_300x300.png?v=1606145937'},
              {'title': 'Fresh Produce', 'link': 'https://gimsap.ca/collections/fresh-produce',
               'image': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/images_63c3097b-031f-4516-9949-670ffd080b9d_300x300.jpg?v=1645134098'},
              {'title': 'Beverages', 'link': 'https://gimsap.ca/collections/beverages-1',
               'image': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/81vXjO077mL._SY445_300x300.jpg?v=1647973626'},
              {'title': 'Beauty Products', 'link': 'https://gimsap.ca/collections/beverages',
               'image': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/924e0f6e-709b-4ce8-ac3e-8133fd0d1724_1.62c8e6d292460fa33ed5ec14f343609f_300x300.jpg?v=1644957926'}]

collection_product = [
    {'id': 1, 'link': 'https://gimsap.ca/collections/dry-food/products/mr-johns-ripe-spicy-plantain-chips',
     'name': "Mr. John's Ripe Spicy Plantain Chips", 'price': '$1.50'},
    {'id': 2, 'link': 'https://gimsap.ca/collections/dry-food/products/fanta-300ml-bottle',
     'name': 'Fanta 300ml Glass Bottle', 'price': '$1.75',
     'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/Mock-Up-MrJ-YELLOW70g_300x300.jpg?v=1603115269'},
    {'id': 3, 'link': 'https://gimsap.ca/collections/dry-food/products/the-noble-plantain-chips-naturally-sweet-130g',
     'name': 'Noble Plantain Chips - Naturally Sweet', 'price': '$2.50',
     'image_url': 'https://cdn.shopify.com/s/files/1/0495/6933/3413/products/81vXjO077mL._SY445_300x300.jpg?v=1647973626'}]


class Gimsap:
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
        self.collection = []
        self.collection_products = []
        super(Gimsap, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(BASE_URL)
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='a[class="js-toggle-login-modal"]'
        ).click()
        self.driver.find_element(
            by=By.ID, value="password"
        ).send_keys("xWRLuaaiw48B")
        self.driver.find_element(
            by=By.CSS_SELECTOR, value='input[class="btn password-page__login-form__submit"]'
        ).click()

    def get_collections(self):
        templates = self.driver.find_elements(
            by=By.CSS_SELECTOR, value='div[class="grid__item medium-down--one-half one-quarter text-center"]'
        )
        id = 0
        for element in templates:
            link = element.find_element(
                by=By.CSS_SELECTOR, value='a[class="grid-link"]').get_attribute('href')
            title = element.find_element(
                by=By.TAG_NAME, value='a').find_element(
                by=By.CLASS_NAME, value='grid-link__title').get_attribute('innerHTML').strip()
            image_url = element.find_element(
                by=By.CSS_SELECTOR, value='a[class="grid-link"]').find_element(
                by=By.CSS_SELECTOR, value='span[class="grid-link__image grid-link__image--collection"]').find_element(
                by=By.CSS_SELECTOR, value='span[class="grid-link__image-centered"]').find_element(
                by=By.CSS_SELECTOR, value='div[class="collection__grid-image-wrapper supports-js"]').find_element(
                by=By.TAG_NAME, value='div').find_element(
                by=By.TAG_NAME, value='img').get_attribute('src')

            self.collection.append(
                {
                    'id': id,
                    "title": title,
                    "link": link,
                    "image": image_url,
                }
            )
            id += 1
            print(id)

    def get_collection_products(self):
        for pages in self.collection:
            self.driver.get(pages['link'])
            self.get_products(pages['id'])
            self.collection[int(pages['id'])].update(
                {'products': self.collection_products}
            )
            with open('gimsap.json', 'w') as f:
                f.write(f"{self.collection}")
            # after adding all products delete the list again
            self.collection_products = []
        with open('gimsap.json', 'w') as f:
            f.write(f"{self.collection}")

    def get_products(self, _id):
        product_id = 0
        for element in self.driver.find_elements(
                by=By.CSS_SELECTOR,
                value='div[class="grid__item wide--one-fifth large--one-quarter medium-down--one-half"]'
        ):
            print(element.get_attribute('innerHTML'))
            link = element.find_element(By.TAG_NAME, value='div').find_element(
                by=By.TAG_NAME,
                value='a'
            ).get_attribute('href')
            name = element.find_element(By.TAG_NAME, value='div').find_element(
                by=By.TAG_NAME,
                value='a'
            ).find_element(
                By.CSS_SELECTOR,
                value='p[class="grid-link__title"]').get_attribute('innerHTML').strip()
            try:
                price = element.find_element(By.TAG_NAME, value='div').find_element(
                    by=By.TAG_NAME,
                    value='a'
                ).find_element(
                    By.CSS_SELECTOR,
                    value='p[class="grid-link__meta"]').get_attribute('innerHTML').strip()
                # price = element.find_element(By.TAG_NAME, value='div').find_element(
                #     by=By.TAG_NAME,
                #     value='a'
                # ).find_element(
                #     By.CSS_SELECTOR,
                #     value='p[class="grid-link__meta"]').find_element(
                #     By.CSS_SELECTOR,
                #     value='span[class="hidden"]').get_attribute('innerHTML').strip()
            except:
                price = element.find_element(By.TAG_NAME, value='div').find_element(
                    by=By.TAG_NAME,
                    value='a'
                ).find_element(
                    By.CSS_SELECTOR,
                    value='p[class="grid-link__meta"]').get_attribute('innerHTML').strip()

            self.collection_products.append(
                {
                    'id': product_id,
                    'link': link,
                    'name': name,
                    'price': price,
                }
            )
            product_id += 1
        self.get_collection_product_description()

    def get_collection_product_description(self):
        for item in self.collection_products:
            self.driver.get(item['link'])
            print('item id given', item['id'])
            self.get_product_description(item['id'])
            with open('gimsap.json', 'w') as f:
                f.write(f"{self.collection}")

    def get_product_description(self, _id):
        description = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value='div[class="product-description rte"]'
        ).get_attribute('innerHTML').strip()
        try:
            image_url = self.driver.find_element(
                by=By.CSS_SELECTOR,
                value='img[class="product-single__image lazyautosizes lazyloaded"]'
            ).get_attribute('src')
        except:
            image_url = self.driver.find_elements(
                by=By.CSS_SELECTOR,
                value='img[class="product-single__image lazyautosizes ls-is-cached lazyloaded"]'
            )[0].get_attribute('src')
        self.collection_products[_id].update(
            {
                'description': description,
                'image_url': image_url
            }
        )
