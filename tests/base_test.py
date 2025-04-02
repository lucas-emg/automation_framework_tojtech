import unittest
from selenium.webdriver.remote.webdriver import WebDriver
from test_classes.misc.webdriver_factory import webdriver_factory


class BaseTest(unittest.TestCase):
    driver: WebDriver

    def setUp(self) -> None:
        self.driver = webdriver_factory(browser="Chrome")
        self.driver.get("https://shopping.beeyor.com/")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
