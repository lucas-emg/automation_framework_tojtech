from selenium.webdriver.remote.webdriver import WebDriver
from test_classes.misc.locator import Locator
from test_classes.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    login_page_header_locator = Locator(by=By.XPATH, value="//h2[text()='Login']")
    username_input_locator = Locator(by=By.ID, value="username")
    password_input_locator = Locator(by=By.ID, value="password")
    login_button_locator = Locator(by=By.NAME, value="login")


    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)

    def wait_for_login_page_header(self) -> None:
        self.wait_until_element_is_visible(self.login_page_header_locator, 15)

    def login(self, email, password) -> None:
        self.input(self.username_input_locator, text=email)
        self.input(self.password_input_locator, text=password)
        self.click(self.login_button_locator)