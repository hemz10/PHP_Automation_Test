from selenium.webdriver.common.by import By


class FlightPage:
    def __init__(self, driver):
        self.driver = driver

    trip = (By.ID, "round-trip")
    flyingFrom = (By.CSS_SELECTOR, "[placeholder = 'Flying From']")
    city = (By.XPATH, "//div[@class = 'autocomplete-result']/div/strong")
    flyingTo = (By.CSS_SELECTOR, "[placeholder = 'To Destination']")
    departure = (By.ID, "departure")
    month = (By.CSS_SELECTOR, "[class = 'switch']")
    nextMonth = (By.XPATH, "//table[@class = ' table-condensed']/thead[1]/tr[1]/th[3]")
    dates = (By.CSS_SELECTOR, "[class = 'day ']")
    passenger = (By.CSS_SELECTOR, "[class *= 'd-block']")
    adult = (By.XPATH, "//div[contains(@class, 'dropdown-menu')]/div[1]/div[1]/div[1]/div[2]")
    child = (By.XPATH, "//div[contains(@class, 'dropdown-menu')]/div[2]/div[1]/div[1]/div[2]")
    infant = (By.XPATH, "//div[contains(@class, 'dropdown-menu')]/div[3]/div[1]/div[1]/div[2]")
    search = (By.ID, "flights-search")

    def roundTrip(self):
        return self.driver.find_element(*FlightPage.trip)

    def getFlyingFrom(self):
        return self.driver.find_element(*FlightPage.flyingFrom)

    def getCity(self):
        return self.driver.find_elements(*FlightPage.city)

    def getFlyingTo(self):
        return self.driver.find_element(*FlightPage.flyingTo)

    def getDeparture(self):
        return self.driver.find_element(*FlightPage.departure)

    def getMonth(self):
        return self.driver.find_element(*FlightPage.month)

    def getNextMonth(self):
        return self.driver.find_element(*FlightPage.nextMonth)

    def getDates(self):
        return self.driver.find_elements(*FlightPage.dates)

    def getPassenger(self):
        return self.driver.find_element(*FlightPage.passenger)

    def getAdultCount(self):
        return self.driver.find_element(*FlightPage.adult)

    def getChildCount(self):
        return self.driver.find_element(*FlightPage.child)

    def getInfantCount(self):
        return self.driver.find_element(*FlightPage.infant)

    def Search(self):
        return self.driver.find_element(*FlightPage.search)
