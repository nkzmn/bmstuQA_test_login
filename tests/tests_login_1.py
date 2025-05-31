import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://berpress.github.io/selenium-login-demo/'

class TestLogin (unittest.TestCase):
    def test_add_valid_data (self):
        # здесь позитивный тест (успешная авторизация с валидными данными)
        # login: admin
        # password: password

        # открыть страницу
        driver = webdriver.Chrome()
        driver.get(URL)

        # находим все элементы на странице
        name = driver.find_element (By.ID,'username')
        password = driver.find_element (By.ID,'password')
        btn_ok = driver.find_element (By.ID,'login-btn')

        # выполняем действия и заполняем поля
        name.send_keys('admin')
        password.send_keys('password')
        time.sleep(2)
        btn_ok.click()
        time.sleep(2)
        driver.quit()

        pass


    def test_add_invalid_data (self):
        # здесь позитивный тест (успешная авторизация с валидными данными)
        # login: admin
        # password: password

        # открыть страницу
        driver = webdriver.Chrome()
        driver.get(URL)

        # находим все элементы на странице
        name = driver.find_element (By.ID,'username')
        password = driver.find_element (By.ID,'password')
        btn_ok = driver.find_element (By.ID,'login-btn')

        # выполняем действия и заполняем поля
        name.send_keys('ad')
        password.send_keys('pass')
        time.sleep(2)
        btn_ok.click()
        time.sleep(2)
        driver.quit()

        pass
