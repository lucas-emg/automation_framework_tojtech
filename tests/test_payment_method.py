from test_classes.pages.home_page import HomePage
from test_classes.pages.login_page import LoginPage
from test_classes.pages.my_account_page import MyAccountPage
import pytest
from test_classes.pages.payment_method_page import PaymentMethodPage
from tests.base_test import BaseTest

class PaymentMethod(BaseTest):

    @pytest.mark.payment_method
    @pytest.mark.happy_path
    def test_add_payment_method(self):
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
        assert my_account_page.confirm_user_name_is_displayed(username="students customer")

        # Go to Payment Methods
        payment_page = PaymentMethodPage(self.driver)
        payment_page.add_card_number(card="4242424242424242",expiry="12/30",cvc="123",zip_code="12345")

        #assert card was added
        assert payment_page.is_card_added()
