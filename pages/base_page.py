from selenium.common.exceptions import NoSuchElementException
from.locators import AccountLocators
from .locators import HeaderLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_account_page(self):
        link = self.browser.find_element(*HeaderLocators.ACCOUNT_BUTTON)
        link.click()

    def go_to_change_pwd_page(self):
        link = self.browser.find_element(*AccountLocators.CHANGE_PWD_LINK)
        link.click()

    def log_out(self):
        link = self.browser.find_element(*HeaderLocators.LOG_OUT_LINK)
        link.click()

    def go_to_log_in_link(self):
        link = self.browser.find_element(*HeaderLocators.LOGIN_LINK)
        link.click()

    def should_be_logged_in(self):
        assert self.is_element_present(*HeaderLocators.LOG_OUT_LINK), 'User is not logged in: cannot find the Log out button'
