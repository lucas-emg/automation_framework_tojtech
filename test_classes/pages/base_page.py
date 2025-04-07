from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test_classes.misc.locator import Locator


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator: Locator) -> None:
        element = self.driver.find_element(locator.by, locator.value)
        element.click()

    def input(self, locator: Locator, text: str) -> None:
        element = self.driver.find_element(locator.by, locator.value)
        element.clear()
        element.send_keys(text)

    def wait_until_element_is_visible(self, locator: Locator, timeout: int) -> WebElement:
        element = WebDriverWait(self.driver, timeout=timeout).until(ec.visibility_of_element_located((locator.by, locator.value)))
        return element

    def find(self, locator: Locator) -> WebElement:
        element = self.driver.find_element(locator.by, locator.value)
        return element

    def confirm_element_is_present(self, locator: Locator) -> bool:
        element = self.find(locator)
        return element.is_displayed()

    def select_by_visible_text(self, locator: Locator, text: str) -> None:
        element = self.driver.find_element(locator.by, locator.value)
        select_element = Select(element)
        select_element.select_by_visible_text(text)

    def scroll_into_view(self, locator: Locator) -> None:
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_and_wait(self, locator: Locator, timeout: int) -> None:
        element = WebDriverWait(self.driver, timeout=timeout).until(ec.visibility_of_element_located((locator.by, locator.value)))
        element.click()
