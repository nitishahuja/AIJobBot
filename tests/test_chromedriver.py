from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def test_chromedriver():
    """Test if ChromeDriver can open Google."""
    # Get the absolute path to chromedriver
    driver_path = os.path.abspath("./chromedriver")

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(driver_path))

    # Open Google
    driver.get("https://www.google.com")

    # Verify the page title
    assert "Google" in driver.title

    # Close the browser
    driver.quit()
