import allure
import requests


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("открытие браузера")
    def open(self):
        url = "https://www.market.yandex.ru/"
        self.driver.get(url)
        status_code = requests.get(url).status_code
        return status_code
