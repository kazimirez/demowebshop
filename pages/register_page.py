import pytest
from .locators import HeaderLocators
from .locators import RegisterLocators
from .base_page import BasePage
from .locators import AccountLocators


class RegisterPage(BasePage):

    @pytest.mark.smoke
    def should_be_register_field(self):
        assert self.is_element_present(*RegisterLocators.REGISTER_FIELD), 'Register button not present'

    def should_be_register_result_page(self):
        expected_url = 'http://demowebshop.tricentis.com/registerresult/1'
        actual_url = self.browser.current_url
        assert expected_url == actual_url, 'registeration failed: wrong url after registration attempt'

    def register_new_user(self, first_name, last_name, email, pwd):
        self.browser.find_element(*RegisterLocators.MALE_RADIOBUTTON).click()
        self.browser.find_element(*RegisterLocators.FIRSTNAME_FIELD).send_keys(first_name)
        self.browser.find_element(*RegisterLocators.LASTNAME_FIELD).send_keys(last_name)
        self.browser.find_element(*RegisterLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*RegisterLocators.PASSWORD_FIELD).send_keys(pwd)
        self.browser.find_element(*RegisterLocators.CONFIRM_PASSWORD_FIELD).send_keys(pwd)
        self.browser.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    def log_in(self, email, pwd):
        self.browser.find_element(*RegisterLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*RegisterLocators.PASSWORD_FIELD).send_keys(pwd)
        self.browser.find_element(*RegisterLocators.LOG_IN_BUTTON).click()

    def change_pwd(self, old_pwd, new_pwd):
        self.browser.find_element(*AccountLocators.OLD_PWD_FIELD).send_keys(old_pwd)
        self.browser.find_element(*AccountLocators.NEW_PWD_FIELD).send_keys(new_pwd)
        self.browser.find_element(*AccountLocators.NEW_PWD_REPEAT_FIELD).send_keys(new_pwd)
        self.browser.find_element(*AccountLocators.CHANGE_PWD_BUTTON).click()

    def should_be_success_pwd_change(self):
        result_message = self.browser.find_element(*AccountLocators.CHANGE_PWD_RESULT).text
        print(result_message)
        assert result_message == "Password was changed", 'result message is not looking good'






