from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators
from .login_page import LoginPage

class BasketPage(BasePage):
    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_BASKET_ITEMS), \
        "Basket is not empty."

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), \
        "There is no message about empty basket."



    