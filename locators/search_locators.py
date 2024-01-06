from selenium.webdriver.common.by import By


class SearchPageLocators:
    # Локаторы для страницы поиска товара
    DELIVERY_TIME = (By.XPATH, "//span[contains(text(), 'Сегодня или завтра')]")
    SERIES = (By.XPATH, "(//span[contains(text(), 'Redmi Note')])[last()]")
    CONDITION_OF_PRODUCT = (By.XPATH, "//span[contains(text(), 'Новый')]")
    BUTTON_TO_BASKET = (
        By.XPATH,
        "//button[@type='button']//span[contains(text(), 'корзину')]",
    )
    TITLE_MODAL_WINDOW = (By.XPATH, "//h2[text()='Товар успешно добавлен в корзину']")
    BUTTON_GO_TO_BASKET = (
        By.XPATH,
        "//button[@type='button']//span[contains(text(), 'Перейти')]",
    )
    TITLE_OF_BASKET = (By.XPATH, "//h1[text()='Корзина']")
