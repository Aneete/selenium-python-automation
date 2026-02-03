from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    message_text = (By.ID, "flash")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_message(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(
            EC.visibility_of_element_located(self.message_text)
        ).text

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)
