from selenium.webdriver.common.by import By


class BasketPageLocators:
    # Локаторы для страницы корзины
    NAME_PRODUCT = (By.XPATH, "//div[@data-baobab-name='title']//a")
