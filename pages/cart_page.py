from selenium.webdriver.common.by import By


class CartPage:

    FLIGHT_INFO = (By.CSS_SELECTOR, "#form .flight-info")
    PAYMENT_FORM = (By.CSS_SELECTOR, "#form #payment")
    SELECTED_FLIGHTS_DATA = (By.CSS_SELECTOR, ".journey>tbody[data-id]")

    def __init__(self, methods):
        self.methods = methods
        self.check()

    def check(self):
        self.methods.wait_for_element(self.FLIGHT_INFO)
        self.methods.wait_for_element(self.PAYMENT_FORM)

    def get_flights_data(self):
        return self.methods.wait_for_element(self.SELECTED_FLIGHTS_DATA).get_attribute("data-id")
