import time

from test_classes.pages.cart_page import CartPage
from test_classes.pages.checkout_page import CheckoutPage
from test_classes.pages.shop_page import ShopPage
from tests.base_test import BaseTest


class TestUserUnableToPlaceOrder(BaseTest):

    def test_user_unable_to_place_order(self):


        # Confirm shop page is loaded and click on add to cart on cool bug product
        shop_page = ShopPage(self.driver)
        shop_page.wait_for_shop_page_header()
        shop_page.add_a_product_to_cart()
        shop_page.click_on_view_cart_of_a_product()

        # Click on proceed to checkout button
        cart_page = CartPage(self.driver)
        cart_page.click_on_proceed_to_checkout()

        # Click on place order button
        checkout_page = CheckoutPage(self.driver)
        checkout_page.wait_for_privacy_policy_link()
        checkout_page.click_on_place_order_button()


        # Confirm user is not able to place an order

        error_message_element = checkout_page.user_unable_to_place_order()
        assert error_message_element

