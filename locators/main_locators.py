from selenium.webdriver.common.by import By


class MainPageLocators:
    # Локаторы для главной страницы
    INPUT_TEXT_IN_SEARCH = (By.CSS_SELECTOR, "input[id='header-search']")
    BUTTON_FIND = (By.CSS_SELECTOR, "button[type='submit']")
    NAME_PRODUCT = (By.XPATH, "//span[contains(text(), 'Смартфон Xiaomi')]")
