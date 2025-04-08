import time

from selenium.webdriver.remote.webdriver import WebDriver
from test_classes.misc.locator import Locator
from test_classes.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MyAccountPage(BasePage):

    dashboard_locator = Locator(by=By.LINK_TEXT, value="Dashboard")
    address_locator = Locator(by=By.LINK_TEXT, value="Addresses")
    billing_address_edit_locator = Locator(by=By.XPATH, value="//a[@href='https://shopping.beeyor.com/my-account/edit-address/billing/']")

    #locators for editing billing address form
    billing_address_header_locator = Locator(by=By.XPATH, value="//h3[text()='Billing address']")
    billing_address_first_name_locator = Locator(by=By.ID, value="billing_first_name")
    billing_address_last_name_locator = Locator(by=By.ID, value="billing_last_name")
    billing_address_country_dropdown_locator = Locator(by=By.ID, value="select2-billing_country-container")
    billing_address_country_locator = Locator(by=By.XPATH, value="//li[text()='United States (US)']")
    billing_address_street_locator = Locator(by=By.ID, value="billing_address_1")
    billing_address_city_locator = Locator(by=By.ID, value="billing_city")
    billing_address_state_dropdown_locator = Locator(by=By.ID, value="select2-billing_state-container")
    billing_address_state_locator = Locator(by=By.XPATH, value="//li[text()='Arizona']")
    billing_address_zipcode_locator = Locator(by=By.ID, value="billing_postcode")
    billing_address_phone_locator = Locator(by=By.ID, value="billing_phone")
    billing_address_email_locator = Locator(by=By.ID, value="billing_email")
    billing_address_save_button_locator = Locator(by=By.NAME, value="save_address")

    #Success message locator for saving billing address
    saving_billing_address_success_message_locator = Locator(by=By.XPATH, value="//div[@role='alert']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)

    def wait_for_dashboard_link(self) -> None:
        self.wait_until_element_is_visible(self.dashboard_locator, timeout=15)

    def click_on_address_link(self) -> None:
        self.click(self.address_locator)

    def click_on_billing_address_edit_link(self) -> None:
        self.click_and_wait(self.billing_address_edit_locator, timeout=15)

    def fill_out_billing_address(self) -> None:
        self.wait_until_element_is_visible(self.billing_address_header_locator, timeout=15)
        self.input(self.billing_address_first_name_locator, text="Donald")
        self.input(self.billing_address_last_name_locator, text="Trump")
        self.click_and_wait(self.billing_address_country_dropdown_locator, timeout=15)
        self.click(self.billing_address_country_locator)
        self.input(self.billing_address_street_locator, text="Bourbon St")
        self.input(self.billing_address_city_locator, text="Whiskey Town")
        self.click_and_wait(self.billing_address_state_dropdown_locator, timeout=15)
        self.click(self.billing_address_state_locator)
        self.input(self.billing_address_zipcode_locator, text="22345")
        self.input(self.billing_address_phone_locator, text="1234567234")
        self.input(self.billing_address_email_locator, text="email@example.com")
        self.click(self.billing_address_save_button_locator)

    def get_success_message_text(self):
        return self.wait_until_element_is_visible(self.saving_billing_address_success_message_locator, timeout=15).text.lower().strip()