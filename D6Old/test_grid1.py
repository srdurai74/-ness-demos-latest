import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_grid():
    print('Starting test setup')

    # Define Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--remote-allow-origins=*")

    # Set capabilities
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("platformName", "Windows 10")

    # Use webdriver_manager to get the latest ChromeDriver
    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=chrome_options
    )

    # Navigate to a website
    driver.get("https://www.example.com")
    time.sleep(10)  # For demonstration, use WebDriverWait in real tests

    print('Setup completed, test running')

    time.sleep(3)  # For demonstration
    driver.quit()
    print('Test completed, driver quit')
