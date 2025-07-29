from selenium.webdriver.common.by import By

from .base_page import BasePage
from test_classes.helpers.locator import Locator


class EditShippingAddressPage(BasePage):
    shipping_and_billing_address_link_locator = Locator(by=By.LINK_TEXT, value="shipping and billing addresses")
    edit_shipping_address_link_locator = Locator(by=By.LINK_TEXT, value="Edit Shipping address")
    address_street_input_locator = Locator(by=By.ID, value="shipping_address_1")
    save_address_button_locator = Locator(by=By.XPATH, value= "//button[@value='Save address']")
    success_banner_locator = Locator(by=By.XPATH, value="//div[contains(@class, 'is-success')]")


    def click_on_shipping_and_billing_address_link(self):
        self.wait_and_click(self.shipping_and_billing_address_link_locator, timeout=10)

    def click_on_edit_shipping_address_link(self):
        self.wait_and_click(self.edit_shipping_address_link_locator, timeout=10)

    def wait_for_edit_shipping_address_page_to_load(self):
        self.wait_until_element_is_visible(self.address_street_input_locator, timeout=10)

    def clear_street_address(self):
        # Clearing the previous input
        self.find_element(self.address_street_input_locator).clear()

    def change_street_address(self, street_address):
        # Typing street address into street line 1 field
        self.input(self.address_street_input_locator, text=street_address)

        #Clicking on the Save Address button
        self.click(self.save_address_button_locator)

    def confirm_success_banner_is_displayed(self):
        return self.confirm_element_is_displayed(self.success_banner_locator)

