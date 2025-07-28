from .base_test import BaseTest
from test_classes.pages.home_page import HomePage
from test_classes.pages.login_page import LoginPage
from test_classes.pages.my_account_page import MyAccountPage


class TestLogin(BaseTest):

    @pytest.mark.login
    @pytest.mark.happy_path