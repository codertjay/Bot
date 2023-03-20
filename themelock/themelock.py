from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.themelock.com/"


class Themelock:
    def __init__(self, teardown=True):

        s = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.teardown = teardown
        # keep chrome open
        # self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option(
            "excludeSwitches",
            ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=self.options,
            service=s)
        self.driver.implicitly_wait(50)
        self.collection = []
        super(Themelock, self).__init__()

    def __enter__(self):
        self.driver.get(BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(BASE_URL)

    def get_description_and_quote(self, url):
        self.driver.get(url)
        description = self.driver.find_element(
            by=By.CLASS_NAME, value='descripton'
        ).get_attribute('innerHTML').strip()
        return description

    def get_collections(self, page):
        templates = self.driver.find_elements(
            by=By.CLASS_NAME, value='short'
        )
        for element in templates:
            title = element.find_element(
                by=By.CSS_SELECTOR, value='div[class="news-titles"]').find_element(
                by=By.TAG_NAME, value='h3').find_element(
                by=By.TAG_NAME, value='a').get_attribute('innerHTML')
            link = element.find_element(
                by=By.CSS_SELECTOR, value='div[class="news-titles"]').find_element(
                by=By.TAG_NAME, value='h3').find_element(
                by=By.TAG_NAME, value='a').get_attribute('href')
            image = element.find_element(
                by=By.CSS_SELECTOR, value='div[class="img-shorts news"]').find_element(
                by=By.TAG_NAME, value='a').find_element(
                by=By.TAG_NAME, value='img').get_attribute('src')
            short_description = element.find_element(
                by=By.CSS_SELECTOR, value='div[class="descripton"]').get_attribute('innerHTML').strip()
            category = element.find_element(
                by=By.CSS_SELECTOR, value='div[class="categ"]').find_elements(
                by=By.TAG_NAME, value='a')

            tags = []
            for item in category:
                tags.append(item.get_attribute('innerHTML'))
            self.collection.append(
                {
                    "page": page,
                    "title": title,
                    "link": link,
                    "image": image,
                    "tags": tags,
                    "short_description": short_description,
                    "description": None,
                }
            )
            with open('themelock.json', 'w') as f:
                f.write(f"{self.collection}")

    def next_page(self, id):
        self.driver.get(f'https://www.themelock.com/pag/{id}/')

    def template_list(self):
        i = 1
        while i < 3149:
            self.next_page(i)
            self.get_collections(i)
            i += 1
