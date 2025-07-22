from .base_page import BasePage
from selenium.webdriver.common.by import By
from test_classes.helpers.locator import Locator


class HomePage(BasePage):
    login_link_locator = Locator(by=By.LINK_TEXT, value="Login")

    def click_on_login_button(self):
        self.wait_and_click(self.login_link_locator, timeout=10)
