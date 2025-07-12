import unittest
from select.webdriver.remote.webdriver import WebDriver
from test_classes.helpers.webdriver_factory import webdriver_factory


class BaseTest(unittest.TestCase):
    """
    A class that will perform everything that is needed in the beginning of the test and in the end of the test.
    Methods for interactions that exists in entire application.
    """
    driver: WebDriver

    def setUp(self) -> None:
        """
        Method that runs in the beginning of every test.
        This method:
        - Creates an instance of the driver by using the webdriver_factory function
        -Assigns it to the self.driver variable
        -It navigates to the Shopping Beeyor page
        - Maximize the window
        """
        self.driver = webdriver_factory(browser="Chrome")
        self.driver.get("http://staging.shopping.beeyor.com/")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        """
        Method that runs in the end of every test.
        This method:
        - quits the driver
        """
        self.driver.quit()