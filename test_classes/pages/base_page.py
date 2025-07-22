from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from test_classes.helpers.locator import Locator


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator: Locator):
        element = self.driver.find_element(locator.by, locator.value)
        element.click()

    def input(self, locator: Locator, text):
        element = self.driver.find_element(locator.by, locator.value)
        element.send_keys(text)

    def wait_until_element_is_visible(self, locator: Locator, timeout):
        WebDriverWait(self.driver, timeout=timeout).until(expected_conditions.visibility_of_element_located((locator.by, locator.value)))

    def wait_and_click(self, locator: Locator, timeout):
        element = WebDriverWait(self.driver, timeout=timeout).until(expected_conditions.visibility_of_element_located((locator.by, locator.value)))
        element.click()

    def confirm_element_is_displayed(self, locator: Locator):
        element = WebDriverWait(self.driver, timeout=20).until(expected_conditions.visibility_of_element_located((locator.by, locator.value)))
        return element.is_displayed()
