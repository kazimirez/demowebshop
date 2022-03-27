from .base_page import BasePage
from .locators import HeaderLocators


class MainPage(BasePage):

    def should_be_register_button(self):
        assert self.is_element_present(*HeaderLocators.REGISTER_BUTTON)

    def should_be_login_button(self):
        assert self.is_element_present(*HeaderLocators.LOGIN_BUTTON)

    def should_be_cart_button(self):
        assert self.is_element_present(*HeaderLocators.CART_BUTTON)

    def should_be_wishlist_button(self):
        assert self.is_element_present(*HeaderLocators.WISHLIST_BUTTON)

