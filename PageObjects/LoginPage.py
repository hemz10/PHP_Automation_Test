from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, "[placeholder= 'Email']")
    password = (By.CSS_SELECTOR, "[placeholder= 'Password']")
    login = (By.CSS_SELECTOR, "[class = 'ladda-label']")

    def getEmail(self):
        return self.driver.find_element(*LoginPage.email)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLogin(self):
        return self.driver.find_element(*LoginPage.login)

    def getURL(self):
        return self.driver.current_url
