import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.LoginPage import LoginPage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.phptravels.net/login")
    driver.maximize_window()
    request.cls.driver = driver
    login = LoginPage(driver)
    login.getEmail().send_keys("user@phptravels.com")
    login.getPassword().send_keys("demouser")
    login.getLogin().click()
    yield
    driver.close()
