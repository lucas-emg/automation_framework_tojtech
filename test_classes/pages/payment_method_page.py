from selenium.webdriver.common.by import By
from .base_page import BasePage
from test_classes.helpers.locator import Locator

class PaymentMethodPage(BasePage):
    add_payment_method_locator = Locator(by=By.XPATH, value="//div[@class='woocommerce-MyAccount-content']")

    credit_debit_card_frame_locator = Locator(by=By.CLASS_NAME,value="woocommerce-PaymentMethod woocommerce-PaymentMethod--stripe payment_method_stripe")
    card_number_field_locator = Locator(by=By.CLASS_NAME, value="p-CardNumberInput")
    expiration_date_field_locator = Locator(by=By.ID, value="eField-expiryInput")
    cvc_field_locator = Locator(by=By.ID, value="Field-cvcInput")
    zip_code_field_locator = Locator(by=By.ID, value="Field-postalCodeInput")
    success_message_locator = Locator(by=By.LINK_TEXT, value='Payment method successfully added.')

    def wait_for_credit_debit_card_page_to_load(self):
        self.wait_until_element_is_visible(self.credit_debit_card_frame_locator, timeout=10)

    def switch_to_iframe(self):
        iframe = self.wait_until_element_is_visible(self.credit_debit_card_frame_locator,timeout=10)
        self.driver.switch_to.frame(iframe)

    def add_card_number(self, card, expiry, cvc, zip_code):
        self.input(self.card_number_field_locator, card)
        self.input(self.expiration_date_field_locator, expiry)
        self.input(self.cvc_field_locator, cvc)
        self.input(self.zip_code_field_locator, zip_code)
        self.click(self.add_payment_method_locator)


    def is_card_added(self):
        message = self.confirm_element_is_displayed(self.success_message_locator)
        return 'payment method successfully added' in message


