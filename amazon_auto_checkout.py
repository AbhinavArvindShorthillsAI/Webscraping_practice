from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Amazon India
driver.get("https://www.amazon.in/")

#  Wait for search bar and search for "OnePlus 13"
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("OnePlus 13")
search_box.send_keys(Keys.RETURN)  # Press Enter

#  Define the expected product title
expected_text = "OnePlus 13 | Smarter with OnePlus AI (12GB RAM, 256GB Storage Midnight Ocean)"

# Find the product with the exact text and click it
try:
    product_link = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{expected_text}')]")))
    product_link.click()
    print("Found and clicked on the exact product!")
except:
    print(" Product not found!")
    driver.quit()
    exit()

# Switch to the new tab (if Amazon opens a new tab)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])

#  Wait for "Add to Cart" button and click it
try:
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()
    print("  Successfully added 'OnePlus 13' to cart!")
except:
    print(" 'Add to Cart' button not found! Trying alternative method...")
    try:
        # Alternative: Try clicking "Buy Now" instead
        buy_now_button = wait.until(EC.element_to_be_clickable((By.ID, "buy-now-button")))
        buy_now_button.click()
        time.sleep(5)
        print(" 'Buy Now' button clicked instead of 'Add to Cart'.")
    except:
        print(" Could not find 'Add to Cart' or 'Buy Now'. Exiting.")

#  Go back to home page
driver.back()
driver.back()

print(" Returned to Amazon Home Page.")
time.sleep(5)

#  Close browser
driver.quit()
