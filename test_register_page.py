import pytest
import time
from .test_data import TestLinks
from .pages.register_page import RegisterPage
from .test_data import TestAccounts


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

    def test_login_existing_user(self, browser):
        page = RegisterPage(browser, TestLinks.main_page_link)
        page.open()
        page.go_to_log_in_link()
        page.log_in(TestAccounts.email, TestAccounts.pwd)

    def test_user_can_change_pwd(self, browser):
        page = RegisterPage(browser, TestLinks.main_page_link)
        page.open()
        page.go_to_log_in_link()
        page.log_in(TestAccounts.email, TestAccounts.pwd)
        page.go_to_account_page()
        page.go_to_change_pwd_page()
        page.change_pwd(TestAccounts.pwd, TestAccounts.pwd)
        page.should_be_success_pwd_change()





# pytest -v -s --tb=line "-m pro" --browser_name=firefox --browser_language=kek test_register_page.py
