from selenium.webdriver.remote.webdriver import WebDriver
from test_classes.misc.locator import Locator
from test_classes.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    proceed_to_checkout_locator = Locator(by=By.XPATH, value="//a[contains(@class, 'checkout-button')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)

    def click_on_proceed_to_checkout(self):
        self.click_and_wait(self.proceed_to_checkout_locator, timeout=15)


