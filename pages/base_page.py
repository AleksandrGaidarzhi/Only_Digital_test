from loguru import logger
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием"""
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logger.error(f"Элемент не найден: {locator}")
            raise

    def get_url(self):
        return self.driver.current_url

    def click_on_element(self, *locator):
        self.find_element(*locator).click()

    def element_is_visible(self, locator, timeout=None):
        """Проверить видимость элемента"""
        try:
            element = self.find_element(locator, timeout)
            return element.is_displayed()
        except (NoSuchElementException, TimeoutException) as e:
            logger.error(f"Unexpected error checking element visibility: {e}")
            return False

    def element_is_clickable(self, locator, timeout=10):
        """Проверяет, кликабелен ли элемент"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator))
            return True
        except Exception as e:
            logger.error(f"Элемент не кликабелен: {e}")
            return False

    def scroll_to_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        item = wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", item)
        try:
            return item.is_displayed()
        except (NoSuchElementException, TimeoutException) as e:
            logger.error(f"Ошибка при прокрутке к элементу: {e}")
            raise

    def window_scroll(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y});")
