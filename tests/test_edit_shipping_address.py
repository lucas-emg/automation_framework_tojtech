from .base_test import BaseTest
from test_classes.pages.home_page import HomePage
from test_classes.pages.login_page import LoginPage
from test_classes.pages.my_account_page import MyAccountPage
from test_classes.pages.edit_shipping_address_page import EditShippingAddressPage
import pytest


class TestEditShippingAddress(BaseTest):

    @pytest.mark.edit_shipping_address
    @pytest.mark.happy_path
    def test_edit_shipping_address(self):
        # Navigates to the Login page
        home_page = HomePage(self.driver)
        home_page.click_on_login_button()

        # Wait for the login page and login
        login_page = LoginPage(self.driver)
        login_page.wait_for_login_page_to_load()
        login_page.log_in(username="students", password="Default1!")

        # Confirm username is displayed
        my_account_page = MyAccountPage(self.driver)
        my_account_page.wait_for_my_account_page_to_load()

        # Click on Shipping and Billing Address link
        shipping_and_billing_address = EditShippingAddressPage(self.driver)
        shipping_and_billing_address.click_on_shipping_and_billing_address_link()

        # Click on Edit Shipping Address link
        edit_shipping_address = EditShippingAddressPage(self.driver)
        edit_shipping_address.click_on_edit_shipping_address_link()

        # Wait for the Edit Shipping Address page
        edit_shipping_address_page = EditShippingAddressPage(self.driver)
        edit_shipping_address_page.wait_for_edit_shipping_address_page_to_load()
        # Clear the previous input
        edit_shipping_address_page.clear_street_address()
        # Change the Street Address line 1 only
        edit_shipping_address_page.change_street_address(street_address="1000 Hollywood Avenue")

        # Confirm the street address line 1 is displayed
        my_account_page = MyAccountPage(self.driver)
        my_account_page.wait_for_my_account_page_to_load()
        assert my_account_page.confirm_new_street_address_line_is_displayed(street_address="1000 Hollywood Avenue")
