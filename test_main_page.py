import pytest
from .pages.main_page import MainPage
from .test_data import TestLinks


@pytest.mark.smoke
def test_should_be_basic_links(browser):
    page = MainPage(browser, TestLinks.main_page_link)
    page.open()
    page.should_be_register_button()
    page.should_be_login_button()
    page.should_be_cart_button()
    page.should_be_wishlist_button()

# pytest -v -s --tb=line "-m smoke" --browser_name=firefox --is_headless=false test_main_page.py
