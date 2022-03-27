from .base_page import BasePage
from .locators import HeaderLocators


class MainPage(BasePage):

    def should_be_register_button(self):
        assert self.is_element_present(*HeaderLocators.REGISTER_BUTTON), 'Register button not present'

    def should_be_login_button(self):
        assert self.is_element_present(*HeaderLocators.LOGIN_BUTTON), 'Login button is not present'

    def should_be_cart_button(self):
        assert self.is_element_present(*HeaderLocators.CART_BUTTON), 'Cart button is not present'

    def should_be_wishlist_button(self):
        assert self.is_element_present(*HeaderLocators.WISHLIST_BUTTON), 'Wishlist button is not present'

