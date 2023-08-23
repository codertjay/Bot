import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(
    options=options,
    service=Service(ChromeDriverManager().install())
)
browser.maximize_window()
browser.get('https://accounts2.hktdc.com/en/login?auth_req=y')
browser.implicitly_wait(10)

file_path = input("Enter the path to the text file: ")

# Open the file in read mode
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove any newline characters from the lines and store them in a list
lines = [line.strip() for line in lines]

inputMassage = input("Enter in the message you would like to send :--")


def startBro(param):
    browser.get("https://sourcing.hktdc.com/")

    wait = WebDriverWait(browser, 10)  # Maximum wait time of 10 seconds
    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[3]/div/header/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/form/input")))

    # Send keys to the element
    element.send_keys(param)

    element.send_keys(Keys.ENTER)


def scrolltobottom():
    SCROLL_PAUSE_TIME = 5

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


unique_links = []


def convert():
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')
    link_list = []

    div_elements = soup.find_all('div', class_='chat-button-container card-chat-now-button css-1mo1q2a egd1lqm0')
    for div in div_elements:
        link = div.find('a')['href']
        link_list.append(link)

    unique_links = list(set(link_list))
    print(unique_links)
    for link in unique_links:
        browser.get(link)
        try:
            if (browser.find_elements(By.XPATH,
                                      '/html/body/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[30]/div[2]/div/div[2]/div/div/div/div[1]/div[3]')):
                browser.find_element(By.XPATH,
                                     '/html/body/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[30]/div[2]/div/div[2]/div/div/div/div[1]/div[3]')
                print("already msg sent")
            else:
                element_xpath = '/html/body/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[30]/div[2]/div/div[4]/div[1]/textarea'
                element = browser.find_element(By.XPATH, element_xpath)
                # Click on the element
                element.click()

                # Send Ctrl + A to select all text
                element.send_keys(Keys.CONTROL, 'a')

                # Send Backspace to delete the selected text
                element.send_keys(Keys.BACKSPACE)

                wait = WebDriverWait(browser, 10)
                element.send_keys(inputMassage)
                element = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                     "/html/body/div[3]/div[3]/div[2]/div/div[1]/div[1]/div[30]/div[2]/div/div[4]/div[1]/div[3]/div[2]/div[2]/button")))
                element.click()

        except:
            pass
            # return True


for line in lines:
    startBro(line)

    scrolltobottom()

    convert()

    time.sleep(180)
