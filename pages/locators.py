from selenium.webdriver.common.by import By

main_page_link = 'http://demowebshop.tricentis.com'
register_link = 'http://demowebshop.tricentis.com/register'


class HeaderLocators:
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".ico-register")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".ico-login")
    CART_BUTTON = (By.CSS_SELECTOR, "#topcartlink .cart-label")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".ico-wishlist .cart-label")
