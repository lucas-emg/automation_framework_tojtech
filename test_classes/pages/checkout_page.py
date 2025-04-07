from selenium.webdriver.remote.webdriver import WebDriver
from test_classes.misc.locator import Locator
from test_classes.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):

    place_order_locator = Locator(by=By.ID, value="place_order")
    privacy_policy_locator = Locator(by=By.LINK_TEXT, value="privacy policy")
    error_message_locator = Locator(by=By.XPATH, value="//ul[@role='alert']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)

    def wait_for_privacy_policy_link(self):
        self.wait_until_element_is_visible(self.privacy_policy_locator, timeout=15)

    def click_on_place_order_button(self) -> None:
        # Scroll to the button first
        button = self.wait_until_element_is_visible(self.place_order_locator, timeout=15)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)

        # Then click using JavaScript
        self.driver.execute_script("arguments[0].click();", button)

    def user_unable_to_place_order(self):
        element = self.wait_until_element_is_visible(self.error_message_locator, timeout=15)
        return element