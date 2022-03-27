import pytest
import time
from .pages.locators import register_link
from .pages.register_page import RegisterPage


@pytest.mark.smoke
def test_should_be_basic_fields(browser):
    page = RegisterPage(browser, register_link)
    page.open()
    page.should_be_register_field()


def test_register_new_user(browser):
    page = RegisterPage(browser, register_link)
    page.open()
    email = str(time.time()) + "@mail.com"
    password = "testpassword"
    first_name = "tester"
    last_name = "tester"
    page.register_new_user(first_name, last_name, email, password)
    page.should_be_register_result_page()


# pytest -v -s --tb=line "-m unmarked"  test_register_page.py
