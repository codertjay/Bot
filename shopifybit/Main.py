from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from webdriver_manager.chrome import ChromeDriverManager


def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = 'CENSORED'
        msg['To'] = 'CENSORED'
        msg['Subject'] = 'Automation Failure Alert'
        body = 'The automation script failed to execute. Please check the application.'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(msg['From'], 'CENSORED')
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except Exception as e:
        print("Email could not be sent. Error: ", str(e))


# Specify the path to the ChromeDriver executable
# chromedriver_path = '/usr/local/bin'

# Create a Service object with the path to ChromeDriver
# service = Service(chromedriver_path)
service = Service(ChromeDriverManager().install())

# Start the WebDriver session
driver = webdriver.Chrome(service=service)

# Initialize the WebDriverWait with a timeout of 10 seconds
wait = WebDriverWait(driver, 10)
# Navigate to Shopify's login page
driver.get('https://allaquix.com/admin')

username_field = wait.until(EC.presence_of_element_located((By.ID, 'account_email')))
username_field.send_keys('free-samples@allaquix.com')

wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue with Email"]'))).click()
time.sleep(10)
password_field = wait.until(EC.presence_of_element_located((By.ID, 'account_password')))
password_field.send_keys('AL4qRic$V.Wy,7C')

wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in"]'))).click()

time.sleep(2)  # Wait for the page to load after login

for i in range(500):
    try:
        time.sleep(2)
        driver.get('https://allaquix.myshopify.com/admin/customers?segment_id=420220469294')

        first_customer = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[2]")))
        first_customer.click()

        wait.until(EC.element_to_be_clickable((By.ID, "customers-customerProfile-orders-new"))).click()

        browse_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Browse"]')))
        browse_button.click()

        popular_products = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Popular products')]")))
        popular_products.click()

        product_to_select = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@aria-label="Select: TRIAL - AllaQuix High-Performance Stop Bleeding Gauze (LG 2in)"]')))
        product_to_select.click()

        second_button = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@type="button"])[2]')))

        actions = ActionChains(driver)
        actions.move_to_element(second_button).click(second_button).perform()

        collect_payment_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[contains(text(),"Collect payment")]]')))
        collect_payment_button.click()

        mark_as_paid_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[contains(text(),"Mark as paid")]]')))
        mark_as_paid_button.click()

        create_order_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[.//span[contains(text(),"Create Order")]]')))
        create_order_button.click()

    except Exception as e:
        print("Error occurred: ", str(e))
        send_email()  # Send email if an error occurs
        break  # Stop the loop if an error occurs

driver.quit()
