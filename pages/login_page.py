from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.name = (By.ID, 'username')
        self.password = (By.ID, 'password')
        self.btn_ok = (By.ID, 'login-btn')
        self.result = (By.ID, 'result')

    def add_login (self, name, password):
        self.driver.find_element (*self.name).send_keys(name)
        self.driver.find_element (*self.password).send_keys(password)
        self.driver.find_element (*self.btn_ok).click()
