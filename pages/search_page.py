import time
import allure

from locators.search_locators import SearchPageLocators
from pages.actions_page import ActionsPage


class SearchPage(ActionsPage):
    @allure.step("выбрать различные фильтры")
    def choose_different_filters(self):
        self.element_is_present_and_click(SearchPageLocators.DELIVERY_TIME)
        self.element_is_present_and_click(SearchPageLocators.SERIES)
        self.element_is_present_and_click(SearchPageLocators.CONDITION_OF_PRODUCT)
        return True

    @allure.step("добавить в корзину")
    def add_to_basket(self):
        time.sleep(5)
        self.element_is_present_and_click(SearchPageLocators.BUTTON_TO_BASKET)
        title = self.element_is_present_and_get_text(
            SearchPageLocators.TITLE_MODAL_WINDOW
        )
        return title

    @allure.step("перейти в корзину")
    def go_to_basket(self):
        self.element_is_present_and_click(SearchPageLocators.BUTTON_GO_TO_BASKET)
        title = self.element_is_present_and_get_text(SearchPageLocators.TITLE_OF_BASKET)
        return title
