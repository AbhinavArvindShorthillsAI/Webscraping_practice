from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Disable bot detection
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=options)

# Open Gmail login page
driver.get("https://accounts.google.com/signin")

# Increase the wait time to 20 seconds
wait = WebDriverWait(driver, 20)

#  Try locating the email field dynamically
email_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
email_input.send_keys("abhinax03@gmail.com")

#  Click "Next" button using updated class name
next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
next_button.click()

#  Wait for password field to load
password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
password_input.send_keys("Enter your pass")

#  Click "Next" after entering password
next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
next_button.click()

#  Wait for login success (Gmail Inbox)
wait.until(EC.url_contains("mail.google.com"))

print(" Login Successful!")

# Close browser
driver.quit()









# id_login-id for login page
# id_password-id for password
# (These are in the input tag)

# whsOnd zHQkBf-  class for password
# Hvu6D- class for username

# VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b
# class name for next button 

