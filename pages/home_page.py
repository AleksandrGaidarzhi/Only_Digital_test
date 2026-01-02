from pages.base_page import BasePage
from utils.locators import FooterLocators as foot_loc
from loguru import logger


class HomePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.url = url

    def open(self):
        """Открыть главную страницу"""
        logger.info(f"Открытие страницы: {self.url}")
        self.driver.get(self.url)

    def is_footer_present(self):
        """Проверить наличие футера"""
        return self.is_element_present(foot_loc.ROOT)

    def is_footer_visible(self):
        """Проверить видимость футера"""
        return self.is_element_visible(foot_loc.ROOT)

    def is_element_present(self, locator):
        """Проверить наличие элемента"""
        try:
            self.find_element(locator)
            return True
        except Exception as e:
            logger.debug(f"Элемент не найден: {locator}, ошибка: {e}")
            return False

    def scroll_to_element(self, locator):
        """Прокрутить к элементу"""
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            logger.debug(f"Прокручено к элементу: {locator}")
            return True
        except Exception as e:
            logger.error(f"Ошибка при прокрутке к элементу: {e}")
            return False

    def get_footer_text(self):
        """Получить текст футера"""
        try:
            return self.find_element(foot_loc.TEXT).text
        except Exception as e:
            logger.error(f"Ошибка при получении текста футера: {e}")
            return ""