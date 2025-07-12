from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, by, value):
        element = self.driver.find_element(by, value)
        element.click()

    def input(self, by, value):
        element = self.driver.find_element(by, value)
        element.send_keys(text)

    def wait_until_element_is_visible(self, by, value, timeout):
        WebDriver(self.driver, timeout=timeout).until(expected_conditions.visibility_of_element_located((by, value)))


    def wait_and_click(self, by, value, timeout):
        element = WebDriver(self.driver, timeout=timeout).until(expected_conditions.visibility_of_element_located((by, value)))
        element.click()

    def confirm_element_is_displayed(self, by, value):
        element = WebDriver(self.driver, timeout=20).until(expected_conditions.visibility_of_element_located((by, value)))
        return element.is_displayed()
