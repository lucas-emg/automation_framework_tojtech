from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):

    def wait_for_login_page_to_load(self):
        self.wait_until_element_is_visible(by=By.ID, value="username", timeout=10)

    def log_in(self, username, password):
        #Typing username into username field
        self.input(by=By.ID, value="username", text=username)

        #Typing password into password field
        self.input(by=By.ID, value="password", text=password)

        #Clicking on the Log in button
        self.click(by=By.XPATH, value="//button[@name='Login']")

    def confirm_error_banner_is_displayed(self):
        return self.confirm_element_is_displayed(by=By.XPATH, value="//div[contains(@class, 'is-error')]")
