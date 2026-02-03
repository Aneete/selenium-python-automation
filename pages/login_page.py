from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    message_text = (By.ID, "flash")

    def enter_username(self, username):
        self.driver.find_element(self.username_field).send_keys(username)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_message(self):
        return self.driver.find_element(*self.message_text).text

    def enter_password(self, password):
        self.driver.find_element(self.password_field).send_keys(password)
