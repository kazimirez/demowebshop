from .base_page import BasePage
from .locators import LogInLocators


class LogInPage(BasePage):
    def log_in(self, email, pwd):
        self.browser.find_element(*LogInLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LogInLocators.PASSWORD_FIELD).send_keys(pwd)
        self.browser.find_element(*LogInLocators.LOG_IN_BUTTON).click()
