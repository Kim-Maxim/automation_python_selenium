import allure

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class ActionsPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("ждать и ввести текст")
    def element_is_present_and_send_keys(self, locator, text, timeout=5):
        wait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        ).send_keys(text)

    @allure.step("ждать и нажать на элемент")
    def element_is_present_and_click(self, locator, timeout=5):
        wait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        ).click()

    @allure.step("ждать и получить текст")
    def element_is_present_and_get_text(self, locator, timeout=5):
        return (
            wait(self.driver, timeout)
            .until(EC.presence_of_element_located(locator))
            .text
        )
