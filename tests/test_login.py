import time

from base_test import BaseTest
from Test_classes.pages.home_page import HomePage
from Test_classes.pages.login_page import LoginPage
from Test_classes.pages.my_account_page import MyAccount


class TestLogin(BaseTest):

    def test_login_correct_credentials(self):
        # Navigate to the Login page
        home_page = HomePage(self.driver)
        home_page.click_on_login.button()

        # Wait for the login page and login
        login_page = LoginPage(self.driver)
        login_page.wait_for_login_page_to_load()
        login_page.log_in(username="students", password="Default1!")

        # Confirm username is displayed
        my_account_page = MyAccountPage(self.driver)
        assert my_account_page.confirm_user_name_is_displayed(username="Students customer")


        def test_login_incorrect_credentials(self):
            # Navigate to the Login page
            home_page = HomePage(self.driver)
            home_page.click_on_login.button()

            # Wait for the login page and login
            login_page = LoginPage(self.driver)
            login_page.wait_for_login_page_to_load()
            login_page.log_in(username="not_a_user", password="not_a_password")

            assert login_page.confirm_error_banner_is_displayed()

            time.sleep(10)