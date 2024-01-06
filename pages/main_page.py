import allure

from locators.main_locators import MainPageLocators
from pages.actions_page import ActionsPage


class MainPage(ActionsPage):
    @allure.step("ввести текст в строку поиска")
    def input_text_in_search(self):
        self.element_is_present_and_send_keys(
            MainPageLocators.INPUT_TEXT_IN_SEARCH, "Cмартфон Xiaomi"
        )
        self.element_is_present_and_click(MainPageLocators.BUTTON_FIND)
        name_product = self.element_is_present_and_get_text(
            MainPageLocators.NAME_PRODUCT
        )
        return name_product
