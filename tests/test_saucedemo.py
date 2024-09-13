import pytest
import allure
from selene import be, by, have, command, browser
from saucedemo_tests.web.buy_product import buy_product
import os

@allure.parent_suite('Web')
@allure.story('Saucedemo')
@allure.label('owner', 'ischenkoalex')
@allure.title('Buy product')
def test_buy_product():
    with allure.step('Открываем браузер и сайт'):
        buy_product.open()

    with allure.step('Заполняем форму входа'):
        buy_product.fill_entry_from()

    with allure.step('Ищем продукт по названию'):
        buy_product.check_product()

    with allure.step('Добавляем продукт в корзину'):
        buy_product.add_to_cart()

    with allure.step('Переходим в корзину'):
        buy_product.go_to_cart()

    with allure.step('Проверяем продукт в корзине'):
        buy_product.check_product_in_cart()

    with allure.step('Переходим на шаг покупки'):
        buy_product.checkout()

    with allure.step('Заполняем форму покупки'):
        buy_product.fill_checkout_from()

    with allure.step('Проверяем полную стоимость'):
        buy_product.check_total_price()

    with allure.step('Подтверждаем покупку'):
        buy_product.finish_checkout()

    with allure.step('Проверяем подтверждения покупки'):
        buy_product.check_confirmation_order()

    with allure.step('Возвращаемся к продуктам'):
        buy_product.go_back_to_products()