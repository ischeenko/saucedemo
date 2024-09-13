import os
from selene import browser, be, by, have
from dotenv import load_dotenv


class BuyProduct:

    def open(self):
        browser.open('/')

    def fill_entry_from(self):
        browser.element('#user-name').type(os.getenv('login'))
        browser.element('#password').type(os.getenv('pass'))
        browser.element('#login-button').click()

    def check_product(self):
        browser.element(by.partial_text('Labs Backpack')).should(be.visible)

    def add_to_cart(self):
        browser.element('#add-to-cart-sauce-labs-backpack').click()

    def go_to_cart(self):
        browser.element('.shopping_cart_link').click()

    def check_product_in_cart(self):
        browser.element('.inventory_item_name').should(have.text('Sauce Labs '
                                                                 'Backpack'))

    def checkout(self):
        browser.element('#checkout').click()

    def fill_checkout_from(self):
        browser.element('#first-name').type(os.getenv('first_name'))
        browser.element('#last-name').type(os.getenv('last_name'))
        browser.element('#postal-code').type(os.getenv('postal_code'))
        browser.element('#continue').click()

    def check_total_price(self):
        browser.element('[data-test="total-label"]').should(have.text('$32.39'))

    def finish_checkout(self):
        browser.element('#finish').click()

    def check_confirmation_order(self):
        browser.element('.title').should(have.text('Checkout: Complete!'))
        browser.element('.complete-header').should(
            have.text('Thank you for your '
                      'order!'))

    def go_back_to_products(self):
        browser.element('#back-to-products').click()


buy_product = BuyProduct()