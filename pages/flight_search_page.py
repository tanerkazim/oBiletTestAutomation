from selenium.webdriver.common.by import By
import time
from pages.flights_page import FlightsPage


class FlightSearchPage:

    SEARCH_CONTAINER = (By.CSS_SELECTOR, "#search-container #search")
    ORIGIN_INPUT = (By.CSS_SELECTOR, "#origin-input")
    DESTINATION_INPUT = (By.CSS_SELECTOR, "#destination-input")
    DEPARTURE_BTN = (By.CSS_SELECTOR, "#departure")
    RETURN_BTN = (By.CSS_SELECTOR, "#return-input-placeholder")
    SEARCH_FLIGHT = (By.CSS_SELECTOR, "#search-button")
    DATE_PICKER = (By.CSS_SELECTOR, ".double-picker")
    CITY_SELECTOR = ".results li[data-value='{}']"
    DAY_SELECTOR = ".calendar-table [data-date='{}']"

    def __init__(self, methods):
        self.methods = methods
        self.check()

    def check(self):
        self.methods.wait_for_element(self.SEARCH_CONTAINER)
        self.methods.wait_for_element(self.ORIGIN_INPUT)
        self.methods.wait_for_element(self.DESTINATION_INPUT)
        self.methods.wait_for_element(self.DEPARTURE_BTN)
        self.methods.wait_for_element(self.RETURN_BTN)
        self.methods.wait_for_element(self.SEARCH_FLIGHT)

    def fill_origin(self):
        self.methods.wait_for_element(self.ORIGIN_INPUT).click()
        self.methods.wait_for_element(self.ORIGIN_INPUT).send_keys(self.methods.get_from_ini("origin_city"))
        self.methods.wait_for_element((By.CSS_SELECTOR, self.CITY_SELECTOR.format(
            self.methods.get_from_ini("origin_city_code")))).click()
        return self.methods.wait_for_element(self.ORIGIN_INPUT).get_attribute("value")

    def fill_destination(self):
        self.methods.wait_for_element(self.DESTINATION_INPUT).click()
        self.methods.wait_for_element(self.DESTINATION_INPUT).send_keys(self.methods.get_from_ini("destination_city"))
        self.methods.wait_for_element((By.CSS_SELECTOR, self.CITY_SELECTOR.format(
            self.methods.get_from_ini("destination_city_code")))).click()
        return self.methods.wait_for_element(self.DESTINATION_INPUT).get_attribute("value")

    def fill_departure(self):
        self.methods.wait_for_element(self.DEPARTURE_BTN).click()
        self.methods.wait_for_element(self.DATE_PICKER)
        self.methods.wait_for_element((By.CSS_SELECTOR, self.DAY_SELECTOR.format(
            self.methods.get_from_ini("departure_date")))).click()
        time.sleep(0.2)

    def fill_return(self):
        self.methods.wait_for_element(self.RETURN_BTN).click()
        self.methods.wait_for_element(self.DATE_PICKER)
        self.methods.wait_for_element((By.CSS_SELECTOR, self.DAY_SELECTOR.format(
            self.methods.get_from_ini("return_date")))).click()
        time.sleep(0.2)

    def search_flights(self):
        self.methods.wait_for_element(self.SEARCH_FLIGHT).click()
        return FlightsPage(self.methods)
