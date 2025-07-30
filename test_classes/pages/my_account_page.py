from selenium.webdriver.common.by import By

from .base_page import BasePage

from test_classes.helpers.locator import Locator


class MyAccountPage(BasePage):
    page_title_link_locator = Locator(by=By.XPATH, value="//h2[.='My Account']")
    payment_methods_link_locator = Locator(by=By.LINK_TEXT, value='Payment methods')
    order_link_locator = Locator(by=By.LINK_TEXT, value='Orders')
    addresses_link_locator = Locator(by=By.LINK_TEXT, value="Addresses")
    account_details_link_locator = Locator(by=By.LINK_TEXT, value="Account details")
    logout_link_locator = Locator(by=By.LINK_TEXT, value="Log out")

    def wait_for_my_account_page_to_load(self):
        self.wait_until_element_is_visible(self.page_title_link_locator, timeout=10)

    def confirm_user_name_is_displayed(self, username):
        username_locator = f"//p//strong[.='{username}']"
        return self.confirm_element_is_displayed(Locator(by=By.XPATH, value=username_locator))

    def click_on_orders_link(self):
        self.click(self.order_link_locator)

    def click_on_addresses_link(self):
        self.click(self.addresses_link_locator)

    def click_on_payment_methods(self):
        self.click(self.payment_methods_link_locator)

    def click_on_account_details(self):
        self.click(self.account_details_link_locator)

    def click_on_logout(self):
        self.click(self.logout_link_locator)
    def confirm_new_street_address_line_is_displayed(self, street_address):
        shipping_address_locator = f"//div[contains(@class, 'woocommerce-Address')]//address[contains(., '{street_address}')]"
        return self.confirm_element_is_displayed(Locator(by=By.XPATH, value=shipping_address_locator))
