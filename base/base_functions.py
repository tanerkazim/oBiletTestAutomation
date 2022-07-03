import os
import random
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from configparser import ConfigParser


class BaseClass(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.config = ConfigParser()
        self.config.read(os.path.join(os.path.dirname(__file__), 'settings.ini'), encoding='utf-8')

    def get_driver(self):
        """
        Sets up chrome driver and returns
        :return: Chromedriver

        """
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.wait = WebDriverWait(self.driver, timeout=20)
        self.driver.maximize_window()
        self.driver.get(self.get_from_ini("website"))
        return self.driver

    def get_from_ini(self, variable):
        """
        Gets data from settings.ini file
        :param variable: desired variable
        :return: value of variable

        """
        return self.config.get("ALL", variable)

    def wait_for_element(self, selector):
        """
        Waits for element to present
        :param selector: locator of the element to find

        """
        return self.wait.until(ec.element_to_be_clickable(selector))

    def wait_for_all_elements(self, selector):
        """
        Waits for all elements to present
        :param selector: locator of the elements to find

        """
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def element_exists(self, selector):
        """
        Returns true if element present or return false if element not present
        :param selector: locator of the element to be checked for

        """
        try:
            self.wait.until(ec.element_to_be_clickable(selector))
            return True
        except TimeoutException:
            return False

    @staticmethod
    def random_number(first_value, second_value):
        """
        Returns random number between parameters
        :param first_value: beginning value of the range
        :param second_value: last value of the range

        """
        return random.randint(first_value, second_value)
