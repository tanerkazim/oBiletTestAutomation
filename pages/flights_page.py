from selenium.webdriver.common.by import By
from pages.cart_page import CartPage


class FlightsPage:

    DEPARTURE_FLIGHTS_LIST = (By.CSS_SELECTOR, "#outbound-journeys")
    FLIGHTS = (By.CSS_SELECTOR, ".visible .item.journey")
    SELECTION_CONTAINER = (By.CSS_SELECTOR, "#selection.container.visible")
    ECO_FLIGHT_OPTION = (By.CSS_SELECTOR, ".open div.EF")
    RETURN_INPUT = (By.CSS_SELECTOR, "#return-input")
    departure_flight_code = None
    return_flight_code = None

    def __init__(self, methods):
        self.methods = methods
        self.check()

    def check(self):
        self.methods.wait_for_element(self.DEPARTURE_FLIGHTS_LIST)
        self.methods.wait_for_element(self.FLIGHTS)

    def select_random_departure_flight(self):
        is_one_way = self.methods.wait_for_element(self.RETURN_INPUT).get_attribute("value")
        flights = self.methods.wait_for_all_elements(self.FLIGHTS)
        random_flight = self.methods.random_number(0, len(flights)-1)
        self.departure_flight_code = self.methods.wait_for_element(flights[random_flight]).get_attribute("data-id")
        flights[random_flight].click()
        if self.methods.element_exists(self.ECO_FLIGHT_OPTION):
            self.methods.wait_for_element(self.ECO_FLIGHT_OPTION).click()
        if is_one_way == "Tek Yön":
            return CartPage(self.methods)
        else:
            self.methods.wait_for_element(self.SELECTION_CONTAINER)

    def select_random_return_flight(self):
        flights = self.methods.wait_for_all_elements(self.FLIGHTS)
        random_flight = self.methods.random_number(0, len(flights) - 1)
        self.return_flight_code = self.methods.wait_for_element(flights[random_flight]).get_attribute("data-id")
        flights[random_flight].click()
        if self.methods.element_exists(self.ECO_FLIGHT_OPTION):
            self.methods.wait_for_element(self.ECO_FLIGHT_OPTION).click()
        return CartPage(self.methods)
