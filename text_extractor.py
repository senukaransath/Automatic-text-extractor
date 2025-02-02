from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

# Wait for the search bar to load
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# Enter search query and press Enter
search_query = "Innobot Health"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

input("Solve the CAPTCHA and press Enter to continue...")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
)

# Click the first search result
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
first_result.click()

# Wait for the new page to load completely
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# Extract a specific text from the opened page
try:
    special_text = driver.find_element(
        By.TAG_NAME, "p").text
    print(f"🔍 Extracted Text: {special_text}")
except:
    print("❌ Could not extract text.")

driver.quit()
