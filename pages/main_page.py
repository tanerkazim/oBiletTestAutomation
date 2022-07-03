from selenium.webdriver.common.by import By
from pages.login_popup import LoginPopup
from pages.flight_search_page import FlightSearchPage


class MainPage:

    LOGIN_BTN = (By.CSS_SELECTOR, '.login a')
    FLIGHT_SEARCH_BTN = (By.CSS_SELECTOR, '.menu.left a[href*="ucak"]')
    PROFILE_BTN = (By.CSS_SELECTOR, ".menu.right a[href*='profil']")
    SEARCH_CONTAINER = (By.CSS_SELECTOR, "#search-container #search")

    def __init__(self, methods):
        self.methods = methods
        self.check()

    def check(self):
        self.methods.wait_for_element(self.LOGIN_BTN)
        self.methods.wait_for_element(self.FLIGHT_SEARCH_BTN)
        self.methods.wait_for_element(self.SEARCH_CONTAINER)

    def navigate_to_login(self):
        self.methods.wait_for_element(self.LOGIN_BTN).click()
        return LoginPopup(self.methods)

    def navigate_to_flight_search(self):
        self.methods.wait_for_element(self.FLIGHT_SEARCH_BTN).click()
        return FlightSearchPage(self.methods)

    def user_profile_presence(self):
        return self.methods.element_exists(self.PROFILE_BTN)
