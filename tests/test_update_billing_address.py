import time

from test_classes.pages.login_page import LoginPage
from test_classes.pages.my_account_page import MyAccountPage
from test_classes.pages.shop_page import ShopPage
from tests.base_test import BaseTest


class TestUpdateBillingAddress(BaseTest):

    def test_update_billing_address(self):


        #confirm shop page is loaded and click login
        shop_page = ShopPage(self.driver)
        shop_page.wait_for_shop_page_header()
        shop_page.click_on_login_button()

        #confirm login page is loaded and login
        login_page = LoginPage(self.driver)
        login_page.wait_for_login_page_header()
        login_page.login(email="students", password="Default1!")

        #confirm my account page is loaded and click on address link
        my_account_page = MyAccountPage(self.driver)
        my_account_page.wait_for_dashboard_link()
        my_account_page.click_on_address_link()
        my_account_page.click_on_billing_address_edit_link()

        #fill out the billing address form and click save button
        my_account_page.fill_out_billing_address()
        success_message = my_account_page.get_success_message_text()
        assert success_message == "address changed successfully."
