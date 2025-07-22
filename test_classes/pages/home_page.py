from .base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def click_on_login_button(self):
        self.wait_and_click(by=By.LINK_TEXT, value="Login", timeout=10)
