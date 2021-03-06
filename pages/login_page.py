from .base_page import BasePage
from .locators import LoginPageLocators
import re

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert re.search(LoginPageLocators.LOGIN_PAGE_ENDING+"$", self.url), \
            "The current page is not a login page."

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "There is no login form on the page."

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            "There is no registration form in the page."
        
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD1)
        password_field1.send_keys(password)
        conf_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD2)
        conf_password.send_keys(password)
        registr_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registr_button.click()


