from selenium import webdriver
from pages.login_page import LoginPage

URL = 'https://berpress.github.io/selenium-login-demo/'
driver = webdriver.Chrome()

def test_valid():
        # open_site (driver=driver, url = URL)
        driver.get(URL)
        login_page = LoginPage(driver)
        login_page.add_login(name='admin', password='password>')

        assert login_page.result.textContent == 'Успешно! Вход выполнен.'
        driver.quit()


def test_invalid():
    # open_site (driver=driver, url = URL)
    driver.get(URL)
    login_page = LoginPage(driver)
    login_page.add_login(name='ad', password='pass>')

    assert login_page.result.textContent == 'Успешно! Вход выполнен.'
    driver.quit()
