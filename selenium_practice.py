import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class SeleniumTestClass:
    def __init__(self):
        # Update the PATH to include the directory containing chromedriver
        # os.environ['PATH'] += os.pathsep + driver_path
 
        # Create a Service object with the correct path
        # service_obj = Service(driver_path)
 
        # Start the ChromeDriver with the Service object
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
 
    def login_and_check_title(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
 
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
 
        login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
 
        username_input.send_keys("Admin")
        password_input.send_keys("admin123")
        login_button.click()
 
        response_title = self.driver.title
        expected_title = "OrangeHRM"
        if response_title == expected_title:
            print("Login Successful")
        else:
            print("Login Failed")
 
    def close_browser(self):
        # Wait for 10 seconds
        time.sleep(5)
 
        # Close the browser
        self.driver.quit()
 
 
# chromedriver_path = "path to your driver"
 
# Create an instance of the SeleniumTestClass
selenium_test = SeleniumTestClass()
 
# Call the login_and_check_title method
selenium_test.login_and_check_title()
 
# Call the close_browser method
selenium_test.close_browser()