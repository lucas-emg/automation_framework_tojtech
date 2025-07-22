from selenium.webdriver.common.by import By

from .base_page import BasePage


class MyAccountPage(BasePage):

    def wait_for_my_account_page_to_load(self):
        self.wait_until_element_is_visible(by=By.XPATH, value="//h2[.='My account']", timeout=10)

    def confirm_user_name_is_displayed(self, username):
        username_locator = f"//p//strong[.='{username}']"
        return self.confirm_element_is_displayed(by=By.XPATH, value=username_locator)
