import pytest
import time
from .test_data import TestLinks
from .pages.register_page import RegisterPage


@pytest.mark.smoke
class TestSmoke:
    @pytest.mark.pro
    def test_should_be_basic_fields(self, browser):
        page = RegisterPage(browser, TestLinks.register_link)
        page.open()
        page.should_be_register_field()

    def test_register_new_user(self, browser):
        page = RegisterPage(browser, TestLinks.register_link)
        page.open()
        email = str(time.time()) + "@mail.com"
        password = "testpassword"
        first_name = "tester"
        last_name = "tester"
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()

# pytest -v -s --tb=line "-m pro" --browser_name=firefox --is_headless=false test_register_page.py
