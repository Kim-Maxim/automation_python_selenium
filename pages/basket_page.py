import allure

from locators.basket_locators import BasketPageLocators
from pages.actions_page import ActionsPage


class BasketPage(ActionsPage):
    @allure.step("проверить наличие продукта в корзину")
    def check_product(self):
        name_product = self.element_is_present_and_get_text(
            BasketPageLocators.NAME_PRODUCT
        )
        return name_product
