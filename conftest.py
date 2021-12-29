import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:/2019/Temp/chromedriver.exe")
    driver.get("https://www.phptravels.net/login")
    driver.maximize_window()
    request.cls.driver = driver
    login = LoginPage(driver)
    login.getEmail().send_keys("user@phptravels.com")
    login.getPassword().send_keys("demouser")
    login.getLogin().click()
    yield
    driver.close()
