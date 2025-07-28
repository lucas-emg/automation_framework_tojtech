from selenium.webdriver.common.by import By
from .base_page import BasePage
from test_classes.helpers.locator import Locator


class MyAccountPage(BasePage):
    page_title_locator = Locator(by=By.XPATH, value="//h2[.='My Account']")
    payment_methods_locator = Locator(by=By.LINK_TEXT, value='Payment methods')
    order_locator = Locator(by=By.LINK_TEXT, value='Orders')
    addresses_locator = Locator(by=By.LINK_TEXT, value="Addresses")
    account_details_locator = Locator(by=By.LINK_TEXT, value="Account details")
    logout_locator = Locator(by=By.LINK_TEXT, value="Log out")

    def wait_for_my_account_page_to_load(self):
        self.wait_until_element_is_visible(self.page_title_locator, timeout=10)

    def confirm_user_name_is_displayed(self, username):
        username_locator = f"//p//strong[.='{username}']"
        return self.confirm_element_is_displayed(Locator(by=By.XPATH, value=username_locator))

    def go_to_orders(self):
        self.click(self.order_locator)

    def go_to_addresses(self):
        self.click(self.addresses_locator)

    def go_to_payment_methods(self):
        self.click(self.payment_methods_locator)

    def go_to_account_details(self):
        self.click(self.account_details_locator)

    def logout(self):
        self.click(self.logout_locator)