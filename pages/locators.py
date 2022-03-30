from selenium.webdriver.common.by import By




class HeaderLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".ico-register")
    LOGIN_LINK = (By.CSS_SELECTOR, ".ico-login")
    CART_LINK = (By.CSS_SELECTOR, "#topcartlink .cart-label")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".ico-wishlist .cart-label")
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, '.header-links .account')
    LOG_OUT_LINK = (By.CSS_SELECTOR, '.ico-logout')


class RegisterLocators:
    REGISTER_FIELD = (By.CSS_SELECTOR, '.center-2')
    MALE_RADIOBUTTON = (By.CSS_SELECTOR, '#gender-male')
    FEMALE_RADIOBUTTON = (By.CSS_SELECTOR, '#gender-female')
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#FirstName')
    LASTNAME_FIELD = (By.CSS_SELECTOR, '#LastName')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#ConfirmPassword')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register-button')
    LOG_IN_BUTTON = (By.CSS_SELECTOR, '.login-button')


class AccountLocators:
    CHANGE_PWD_LINK = (By.CSS_SELECTOR, 'li:nth-child(7) .inactive')
    OLD_PWD_FIELD = (By.CSS_SELECTOR, '#OldPassword')
    NEW_PWD_FIELD = (By.CSS_SELECTOR, '#NewPassword')
    NEW_PWD_REPEAT_FIELD = (By.CSS_SELECTOR, '#ConfirmNewPassword')
    CHANGE_PWD_BUTTON = (By.CSS_SELECTOR, '.change-password-button')
    CHANGE_PWD_RESULT = (By.CSS_SELECTOR, '.result')

