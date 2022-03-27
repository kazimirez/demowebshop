import pytest
from .pages.locators import main_page_link
from .pages.main_page import MainPage


def test_should_be_basic_links(browser):
    page = MainPage(browser, main_page_link)
    page.open()
    page.should_be_register_button()
    page.should_be_login_button()
    page.should_be_cart_button()
    page.should_be_wishlist_button()

