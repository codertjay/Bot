from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Specify the search query and video link you want to click
search_query = "artificial intelligence"
video_link = "https://www.youtube.com/watch?v=c8W7dRPdIPE&pp=ygUjYXJ0aWZpY2lhbCBpbnRlbGxpZ2VuY2UgZnVsbCBjb3Vyc2U%3D"

# Create a Service object with the path to ChromeDriver
# service = Service(chromedriver_path)
service = Service(ChromeDriverManager().install())

# Start the WebDriver session
driver = webdriver.Chrome(service=service)
# Open YouTube
driver.get("https://www.youtube.com/")

# Find the search input field and enter the search query
search_input = driver.find_element_by_name("search_query")
search_input.send_keys(search_query)
search_input.submit()

# Wait for search results to load
wait = WebDriverWait(driver, 10)
video_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a#video-title")))

# Find the video link in the search results and click on it
for result in video_results:
    if result.get_attribute("href") == video_link:
        result.click()
        break

# Close the browser window
driver.quit()
