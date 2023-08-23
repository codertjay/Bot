import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import time

from webdriver_manager.chrome import ChromeDriverManager

# Set the path for the Chrome WebDriver
driver_path = 'Enter Driver Path'

# Set the path to the Excel file
excel_file_path = 'Eneter Excel File Path'

# Set your Facebook login credentials
facebook_email = 'Enter Email'
facebook_password = 'Enter Email'

# Configure Chrome options to disable notifications
chrome_options = Options()
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--headless')

# Create a new instance of the Chrome driver with the configured options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver = webdriver.Chrome(service=Service(executable_path=driver_path), options=chrome_options)

# Open Facebook and log in
driver.get('https://www.facebook.com')
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
email_input.send_keys(facebook_email)
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pass"]')))
password_input.send_keys(facebook_password)
login_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]')))
login_button.click()

# Wait for a few seconds for Facebook to load fully and the user to log in
time.sleep(5)

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)


# Function to take a screenshot and handle retries
def take_screenshot(link, index):
    max_retries = 3
    for retry in range(max_retries):
        try:
            # Set the page load timeout
            driver.set_page_load_timeout(30)  # Set the timeout to 30 seconds (you can adjust this value)

            # Navigate to the link
            driver.get(link)

            # Wait for the page to load completely
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Take a screenshot of the page
            screenshot = driver.get_screenshot_as_png()
            image = Image.open(BytesIO(screenshot))

            # Save the screenshot as an image file
            screenshot_file_path = f"screenshot_{index}.png"
            image.save(screenshot_file_path)

            # Add the screenshot link to the DataFrame
            screenshot_link = {screenshot_file_path}
            df.at[index, 'Screenshot Link'] = screenshot_link

            # Delay between requests
            time.sleep(2)  # Wait for 2 seconds before moving to the next link.

            return True  # If successful, return True

        except Exception as e:
            print(f"Attempt {retry + 1} failed. Retrying...")
    else:
        print(f"Failed to navigate to the link after {max_retries} attempts.")
        # Set 'Screenshot Link' to "No Website" if all retries fail
        df.at[index, 'Screenshot Link'] = "No Website"
        return False


# Iterate over each link in the 'Links' column
for index, row in df.iterrows():
    link = row['Links']

    try:
        # Check if the link is available
        if pd.notna(link):
            success = take_screenshot(link, index)
            if not success:
                continue
        else:
            # If the link is not available, set 'Screenshot Link' to "No Website"
            df.at[index, 'Screenshot Link'] = "No Website"

    except Exception as e:
        print(f"Error occurred while processing link at index {index}: {str(e)}")
        # Set 'Screenshot Link' to "No Website" if there was an error navigating to the link
        df.at[index, 'Screenshot Link'] = "No Website"

# Save the updated DataFrame to the Excel file
df.to_excel(excel_file_path, index=False)

# Close the browser and WebDriver
driver.quit()
