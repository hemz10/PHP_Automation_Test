from selenium.webdriver.common.by import By


class HotelPage:
    def __init__(self, driver):
        self.driver = driver

    searchcity = (By.CSS_SELECTOR, "[title = ' Search by City']")
    searchbox = (By.CSS_SELECTOR, "[role= 'searchbox']")
    cities = (By.CSS_SELECTOR, "[role = 'option']")
    checkin = (By.CSS_SELECTOR, ".checkin")
    month = (By.XPATH, "//table[@class=' table-condensed']/thead/tr[1]/th[2]")
    next_month = (By.XPATH, "//table[@class=' table-condensed']/thead/tr[1]/th[3]")
    date = (By.CSS_SELECTOR, "[class = 'day ']")
    checkoutdate = (By.XPATH, "//td[@class = 'day '][2]")
    travellers = (By.CSS_SELECTOR, "[class *= travellers]")
    roomcount = (By.XPATH, "//div[contains(@class , 'roomBtn')]/div/div[3]")
    adult = (By.XPATH, "//div[@class='dropdown-item'][2]/div/div/div[2]")
    children = (By.XPATH, "//div[@class='dropdown-item'][3]/div/div/div[2]")
    nationality = (By.CSS_SELECTOR, "[class *= 'nationality']")
    submit = (By.ID, "submit")
    selectedcity = (By.ID, "select2-hotels_city-container")
    finalPage = (By.CSS_SELECTOR, "[class = 'sec__title_list']")


    def searchCity(self):
        return self.driver.find_element(*HotelPage.searchcity)

    def searchBox(self):
        return self.driver.find_element(*HotelPage.searchbox)

    def cityList(self):
        return self.driver.find_elements(*HotelPage.cities)

    def checkIn(self):
        return self.driver.find_element(*HotelPage.checkin)

    def getMonth(self):
        return self.driver.find_element(*HotelPage.month)

    def getNextMonth(self):
        return self.driver.find_element(*HotelPage.next_month)

    def getDate(self):
        return self.driver.find_elements(*HotelPage.date)

    def getCheckoutDate(self):
        return self.driver.find_elements(*HotelPage.checkoutdate)

    def getTravellers(self):
        return self.driver.find_element(*HotelPage.travellers)

    def getRoomCount(self):
        return self.driver.find_element(*HotelPage.roomcount)

    def getAdultCount(self):
        return self.driver.find_element(*HotelPage.adult)

    def getChildCount(self):
        return self.driver.find_element(*HotelPage.children)

    def getNationality(self):
        return self.driver.find_element(*HotelPage.nationality)

    def Search(self):
        return self.driver.find_element(*HotelPage.submit)

    def getSelectedCity(self):
        return self.driver.find_element(*HotelPage.selectedcity)

    def getFinalPage(self):
        return self.driver.find_element(*HotelPage.finalPage)
