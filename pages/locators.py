from selenium.webdriver.common.by import By

main_page_link = 'http://demowebshop.tricentis.com'
register_link = 'http://demowebshop.tricentis.com/register'


class HeaderLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".ico-register")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".ico-login")
    CART_BUTTON = (By.CSS_SELECTOR, "#topcartlink .cart-label")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".ico-wishlist .cart-label")


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



