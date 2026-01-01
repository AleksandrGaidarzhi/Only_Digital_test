from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver, base_url):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open(self, url=''):
        url = self.base_url + url
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def click_on_element(self, *locator):
        self.find_element(*locator).click()

    def scroll_to_elem(self, *locator):
        wait = WebDriverWait(self.driver, 10)
        item = wait.until(EC.presence_of_element_located(*locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", item)
        try:
            return item.is_displayed()
        except NoSuchElementException:
            raise NoSuchElementException
