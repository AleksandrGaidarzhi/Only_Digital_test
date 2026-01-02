import pytest
from selenium import webdriver
from utils.locators import MainPageLocators as main_loc
from utils.locators import FooterLocators as foot_loc
from pages.home_page import HomePage



@pytest.fixture(scope='class')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(6)
    browser.set_window_size(1300, 1280)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestBaseFooter:
    URL = 'https://only.digital/'

    def test_footer_visible(self, browser):
        page = HomePage(browser, self.URL)
        page.open()
        assert page.scroll_to_elem(foot_loc.ROOT) is True




    def test_start_button(self, browser):
        pass





