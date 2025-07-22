from selenium.webdriver.common.by import By

from .base_page import BasePage
from test_classes.helpers.locator import Locator


class LoginPage(BasePage):
    username_input_locator = Locator(by=By.ID, value="username")
    password_input_locator = Locator(by=By.ID, value="password")
    login_button_locator = Locator(by=By.XPATH, value="//button[@name='login']")
    error_banner_locator = Locator(by=By.XPATH, value="//div[contains(@class, 'is-error')]")

    def wait_for_login_page_to_load(self):
        self.wait_until_element_is_visible(self.username_input_locator, timeout=10)

    def log_in(self, username, password):
        # Typing username into the username field
        self.input(self.username_input_locator, text=username)
        # Typing password into the password field
        self.input(self.password_input_locator, text=password)
        # Clicking on the Login button
        self.click(self.login_button_locator)

    def confirm_error_banner_is_displayed(self):
        return self.confirm_element_is_displayed(self.error_banner_locator)

