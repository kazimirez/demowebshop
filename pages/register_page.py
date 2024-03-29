from .locators import RegisterLocators
from .base_page import BasePage


class RegisterPage(BasePage):

    def should_be_register_field(self):
        assert self.is_element_present(
            *RegisterLocators.REGISTER_FIELD), 'Register button is not present'

    def should_be_register_result_page(self):
        expected_url = 'http://demowebshop.tricentis.com/registerresult/1'
        actual_url = self.browser.current_url
        assert expected_url == actual_url, 'registration failed: wrong url after registration attempt'

    def register_new_user(self, first_name, last_name, email, pwd):
        self.browser.find_element(*RegisterLocators.MALE_RADIOBUTTON).click()
        self.browser.find_element(*RegisterLocators.FIRSTNAME_FIELD).send_keys(
            first_name)
        self.browser.find_element(*RegisterLocators.LASTNAME_FIELD).send_keys(
            last_name)
        self.browser.find_element(*RegisterLocators.EMAIL_FIELD).send_keys(
            email)
        self.browser.find_element(*RegisterLocators.PASSWORD_FIELD).send_keys(
            pwd)
        self.browser.find_element(
            *RegisterLocators.CONFIRM_PASSWORD_FIELD).send_keys(pwd)
        self.browser.find_element(*RegisterLocators.REGISTER_BUTTON).click()
