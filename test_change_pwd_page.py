import pytest
from .pages.change_pwd_page import ChangePwdPage
from .test_data import TestLinks, TestAccounts


@pytest.mark.smoke
class TestSmoke:
    def test_user_can_change_pwd(self, browser):
        page = ChangePwdPage(browser, TestLinks.change_pwd_page)
        page.open()
        page.log_in(TestAccounts.email, TestAccounts.pwd)
        page.go_to_account_page()
        page.go_to_change_pwd_page()
        page.change_pwd(TestAccounts.pwd, TestAccounts.pwd)
        page.should_be_success_pwd_change()

# pytest -v -s --tb=line "-m smoke" --browser_name=firefox --is_headless=false test_change_pwd_page.py
