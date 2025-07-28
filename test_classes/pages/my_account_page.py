from selenium.webdriver.common.by import By

from .base_page import BasePage

from test_classes.helpers.locator import Locator


class MyAccountPage(BasePage):
    page_title_locator = Locator(by=By.XPATH, value="//h2[.='My Account']")

    def wait_for_my_account_page_to_load(self):
        self.wait_until_element_is_visible(self.page_title_locator, timeout=10)

    def confirm_user_name_is_displayed(self, username):
        username_locator = f"//p//strong[.='{username}']"
        return self.confirm_element_is_displayed(Locator(by=By.XPATH, value=username_locator))
