from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_PAGE_ENDING = "/login/"
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_FIELD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button[value="Register"]')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ALERT_SUCCESSFUL_ADDING_IN_BASKET = (By.CSS_SELECTOR, 'div.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')
    ACTUAL_NAME_OF_THE_PRODUCT = (By.CSS_SELECTOR, 'div.product_main h1')
    ACTUAL_PRICE_OF_THE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    MESSAGE_WITH_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")

class BasketPageLocators():
    CONTINUE_SHOPPING_LINK = (By.XPATH, '//div[@id="content_inner"]/p/a[@href="/en-gb/"]')
    LIST_OF_BASKET_ITEMS = (By.CSS_SELECTOR, "div .basket-items")





