from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def test_login_page():
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    username = driver.find_element(By.ID,"username")
    username.send_keys("tomsmith")
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(3)
    success_msg = driver.find_element(By.ID,"flash").text
    assert"You logged into a secure area!" in success_msg
    driver.quit()
