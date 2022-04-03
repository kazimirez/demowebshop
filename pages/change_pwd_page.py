from .base_page import BasePage
from .locators import ChangePwdLocators, LogInLocators


class ChangePwdPage(BasePage):
    def change_pwd(self, old_pwd, new_pwd):
        self.browser.find_element(*ChangePwdLocators.OLD_PWD_FIELD).send_keys(old_pwd)
        self.browser.find_element(*ChangePwdLocators.NEW_PWD_FIELD).send_keys(new_pwd)
        self.browser.find_element(*ChangePwdLocators.NEW_PWD_REPEAT_FIELD).send_keys(new_pwd)
        self.browser.find_element(*ChangePwdLocators.CHANGE_PWD_BUTTON).click()

    def should_be_success_pwd_change(self):
        result_message = self.browser.find_element(*ChangePwdLocators.CHANGE_PWD_RESULT).text
        print(result_message)
        assert result_message == "Password was changed", 'result message is not looking good'

    def log_in(self, email, pwd):
        self.browser.find_element(*LogInLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LogInLocators.PASSWORD_FIELD).send_keys(pwd)
        self.browser.find_element(*LogInLocators.LOG_IN_BUTTON).click()
