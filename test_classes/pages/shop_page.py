from selenium.webdriver.remote.webdriver import WebDriver
from test_classes.misc.locator import Locator
from test_classes.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ShopPage(BasePage):

    shop_page_header_locator = Locator(by=By.XPATH, value="//h1[text()='Shop']")
    login_button_locator = Locator(by=By.XPATH, value="//a[@title='Login / Register']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)

    def wait_for_shop_page_header(self) -> None:
        self.wait_until_element_is_visible(self.shop_page_header_locator, 15)

    def click_on_login_button(self) -> None:
        self.click(self.login_button_locator)
