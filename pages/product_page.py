from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_button_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be."
    
    def should_dissappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message should dissapear, but it should not."

    def should_be_correct_name_of_the_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ACTUAL_NAME_OF_THE_PRODUCT),\
        "Product name is not present on the page."
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESSFUL_ADDING_IN_BASKET), \
        "Message about success adding to basket is not present on the page."
        alert_text = self.browser.find_elements \
        (*ProductPageLocators.ALERT_SUCCESSFUL_ADDING_IN_BASKET)[0].text
        product_name = self.browser.find_element \
        (*ProductPageLocators.ACTUAL_NAME_OF_THE_PRODUCT).text
        assert product_name == alert_text, \
        "Names of the product in basket and recently added one in basket do not coincide."

        
    def should_be_correct_price_of_the_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ACTUAL_PRICE_OF_THE_PRODUCT), \
        "Product price is not present on the page."
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRICE_IN_BASKET), \
        "Message about price in basket is not present on the page."
        actual_price = self.browser.find_element \
        (*ProductPageLocators.ACTUAL_PRICE_OF_THE_PRODUCT).text
        price_in_basket = self.browser.find_element \
        (*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert actual_price == price_in_basket, \
        "Total price in basket and actual price of the item do not coincide."

    def should_be_success_adding_in_basket (self):
        self.should_be_correct_name_of_the_product_in_basket()
        self.should_be_correct_price_of_the_product_in_basket()


