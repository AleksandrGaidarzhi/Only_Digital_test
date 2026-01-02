import logging

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = logging.getLogger(__name__)

    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент не найден: {locator}")
            raise

    def get_url(self):
        return self.driver.current_url

    def click_on_element(self, *locator):
        self.find_element(*locator).click()

    def is_element_visible(self, locator, timeout=None):
        """Проверить видимость элемента"""
        try:
            element = self.find_element(locator, timeout)
            return element.is_displayed()
        except:
            return False

    def is_element_clickable(self, locator, timeout=10):
        """Проверяет, кликабелен ли элемент"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator))
            return True
        except:
            return False

    def scroll_to_elem(self, *locator):
        wait = WebDriverWait(self.driver, 10)
        item = wait.until(EC.presence_of_element_located(*locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", item)
        try:
            return item.is_displayed()
        except NoSuchElementException:
            raise NoSuchElementException
