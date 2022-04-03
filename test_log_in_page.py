import pytest
from .pages.log_in_page import LogInPage
from .test_data import TestLinks, TestAccounts


@pytest.mark.smoke
class TestSmoke:
    @pytest.mark.pro
    def test_login_existing_user(self, browser):
        page = LogInPage(browser, TestLinks.main_page_link)
        page.open()
        page.go_to_log_in_link()
        page.log_in(TestAccounts.email, TestAccounts.pwd)
        page.should_be_logged_in()

# pytest -v -s --tb=line "-m smoke" --browser_name=firefox --is_headless=false test_log_in_page.py
