from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    hotel = (By.LINK_TEXT, "Hotels")
    flight = (By.LINK_TEXT, "Flights")
    tour = (By.LINK_TEXT, "Tours")
    cars = (By.LINK_TEXT, "Cars")
    visa = (By.LINK_TEXT, "Visa")
    blog = (By.LINK_TEXT, "Blog")

    def gotoHotel(self):
        return self.driver.find_element(*DashboardPage.hotel)

    def getFlight(self):
        return self.driver.find_element(*DashboardPage.flight)

    def gotoTour(self):
        return self.driver.find_element(*DashboardPage.tour)

