import time

from PageObjects.DashboardPage import DashboardPage
from PageObjects.HotelPage import HotelPage
from Utilities.BaseClass import Baseclass


class TestHotel(Baseclass):
    def test_hotelbooking(self):

        dp = DashboardPage(self.driver)
        hp = HotelPage(self.driver)
        dp.gotoHotel().click()
        hp.searchCity().click()
        # Entering keyword in City searchbar
        hp.searchBox().send_keys("Bang")
        time.sleep(2)
        # Getting list of all cities displayed into a list and search the list to select city we want
        cities = hp.cityList()
        for city in cities:
            if city.text == "Bangalore,India":
                city.click()
                break
        time.sleep(2)
        assert hp.getSelectedCity().text == "Bangalore,India"
        # Clicking on Check in Date
        hp.checkIn().click()
        # Clicking on next until the month we want is displayed
        while hp.getMonth().text != "March 2022":
            hp.getNextMonth().click()
        # Getting list of all dates and searching that list to click on date we want.
        dates = hp.getDate()
        for date in dates:
            if date.text == "15":
                date.click()
                break
        # Checkout date
        checkout = hp.getDate()
        for date in checkout:
            if date.text == "20":
                date.click()
                break
        # Entering Traveller count
        hp.getTravellers().click()
        room = 1
        while room != 2:
            hp.getRoomCount().click()
            room += 1
        adult = 2
        while adult != 6:
            hp.getAdultCount().click()
            adult += 1
        # Clicking on Nationality
        hp.getNationality().click()
        nationality = hp.getNationality()
        self.selectByVisibleText(nationality, "India")
        # Final Search
        hp.Search().click()
        assert "Bangalore" in hp.getFinalPage().text
