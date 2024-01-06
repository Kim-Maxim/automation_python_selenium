import pytest
import allure

from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.search_page import SearchPage


@pytest.mark.smoke
@allure.parent_suite("Stepik")
@allure.suite("Тестовое задание")
@allure.sub_suite("Яндекс Маркет")
@allure.severity(allure.severity_level.BLOCKER)
class TestSmoke:
    """Тест SMOKE всего пути от поиска товара до добавления его в корзину"""

    @allure.title("Открытие браузера")
    def test_open(self, driver):
        """Проверить открытие браузера по ссылке"""
        smoke_test = BasePage(driver)
        status_code = smoke_test.open()
        assert status_code == 200, "Сайт не открылся"

    @allure.title("Ввод текста в строку поиска")
    def test_input_text_in_search(self, driver):
        """Проверить ввод данных в строку поиска на главной странице"""
        smoke_test = MainPage(driver)
        name_product = smoke_test.input_text_in_search()
        assert "Смартфон Xiaomi" in name_product, "Товар не найден или не соответствует"

    @allure.title("Выбор разных фильтров")
    def test_choose_different_filters(self, driver):
        """Проверить выбор различных фильтров на странице поиска товара"""
        smoke_test = SearchPage(driver)
        result = smoke_test.choose_different_filters()
        assert result is True, "Фильтры не выбраны"

    @allure.title("Добавление в корзину")
    def test_add_to_basket(self, driver):
        """Проверить добавление товара на странице поиска товара"""
        smoke_test = SearchPage(driver)
        title = smoke_test.add_to_basket()
        assert title == "Товар успешно добавлен в корзину", "Товар не добавлен"

    @allure.title("Переход в корзину")
    def test_go_to_basket(self, driver):
        """Проверить переход в корзину на странице поиска товара"""
        smoke_test = SearchPage(driver)
        title = smoke_test.go_to_basket()
        assert title == "Корзина", "Переход не был совершен"

    @allure.title("Проверка наличия товара в корзине")
    def test_check_product(self, driver):
        """Проверить наличие добавленного товара на странице корзина"""
        smoke_test = BasketPage(driver)
        name_product = smoke_test.check_product()
        assert (
            "Redmi Note" in name_product
        ), "Товар не был добавлен или не соответствует"
