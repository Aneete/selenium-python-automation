import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_open_google():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    time.sleep(2)
    title = driver.title
    assert "Google" in title
    time.sleep(2)
    driver.quit()
