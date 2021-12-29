from PageObjects.DashboardPage import DashboardPage
from PageObjects.FlightPage import FlightPage
from Utilities.BaseClass import Baseclass


class TestFlight(Baseclass):
    def test_flightBooking(self):
        dp = DashboardPage(self.driver)
        fp = FlightPage(self.driver)
        log = self.getLogger()
        log.info("Clicking on Flights Tab")
        dp.getFlight().click()
        log.info("Clicking on roundtrip radio button")
        fp.roundTrip().click()
        log.info("Entering keywords in search field")
        fp.getFlyingFrom().send_keys("Bang")
        cities = fp.getCity()
        for city in cities:
            if city.text in "Bangalore":
                log.info("Clicking on Bangalore")
                city.click()
                break
        log.info("Entering keyword in to field")
        fp.getFlyingTo().send_keys("Male")
        toCity = fp.getCity()
        for city in toCity:
            if city.text in " Male Intl":
                log.info("Clicking on Maldives")
                city.click()
                break
        fp.getDeparture().click()
        while fp.getMonth().text != "March 2022":
            log.info("Tapping on next until March month is displayed")
            fp.getNextMonth().click()
        dates = fp.getDates()
        for date in dates:
            if date.text == "15":
                date.click()
                break
        checkoutDate = fp.getDates()
        for date in checkoutDate:
            if date.text == "21":
                date.click()
                break
        fp.getPassenger().click()
        adult = 0
        while adult != 4:
            fp.getAdultCount().click()
            adult += 1
        child = 0
        while child != 3:
            fp.getChildCount().click()
            child += 1
        infant = 0
        while infant != 2:
            fp.getInfantCount().click()
            infant += 1
        fp.Search().click()
