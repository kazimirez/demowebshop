import pytest
import time
from .pages.locators import register_link
from .pages.locators import main_page_link
from .pages.register_page import RegisterPage

# test user for login:
email = 'testguestkekw@gmail.ru'
pwd = 'testguestkekw'


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


def test_login_existing_user(browser):
    page = RegisterPage(browser, main_page_link)
    page.open()
    page.go_to_log_in_link()
    page.log_in(email, pwd)


def test_user_can_change_pwd(browser):
    page = RegisterPage(browser, main_page_link)
    page.open()
    page.go_to_log_in_link()
    page.log_in(email, pwd)
    page.go_to_account_page()
    page.go_to_change_pwd_page()
    page.change_pwd(pwd, pwd)
    page.should_be_success_pwd_change()





# pytest -v -s --tb=line "-m unmarked"  test_register_page.py
