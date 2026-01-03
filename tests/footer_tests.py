import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.locators import FooterLocators, AltFooterLocators
from pages.main_page import MainPage
from loguru import logger
import time


@pytest.fixture(scope='class')
def driver():
    """Фикстура для браузера на весь класс тестов"""
    logger.info("Запуск браузера...")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.set_window_size(1300, 1280)
    yield driver
    logger.info("Закрытие браузера...")
    driver.quit()

class BaseTest:
    URL = None
    LOCATOR = None
    @pytest.fixture(scope='class')
    def page(self, driver):
        if self.URL is None:
            raise ValueError("URL must be defined in child class")
        page = MainPage(driver, self.URL)
        page.open()
        logger.info("Страница загружена")
        return page

class TestMainFooter(BaseTest):
    URL = 'https://only.digital'
    LOCATOR = FooterLocators

    def test_footer_presence(self, page):
        page.window_scroll('0', 'document.body.scrollHeight')
        """Тест на наличие футера на странице"""
        logger.info("Проверка наличия футера на странице")
        assert page.element_is_present(self.LOCATOR.ROOT), "Футер не найден на странице"
        # Проверка, что футер видим
        assert page.element_is_visible(self.LOCATOR.ROOT), "Футер не видим на странице"
        logger.success("Футер успешно найден и видим")

    def test_footer_sections_visibility(self, page):
        """Тест на видимость всех основных секций футера"""
        logger.info("Проверка видимости секций футера")

        sections = [
            ("Логотип", self.LOCATOR.LOGO),
            ("Социальные сети", self.LOCATOR.SOCIALS),
            ("Telegram секция", self.LOCATOR.TELEGRAM),
            ("Контакты", self.LOCATOR.CONTACT),
            ("Текст футера", self.LOCATOR.TEXT),
            ("Презентация", self.LOCATOR.DOCUMENTS),
            ("Годы", self.LOCATOR.YEAR),
            ("Копирайтер", self.LOCATOR.COPYRIGHTS),
            ("Политика конфиденциальности", self.LOCATOR.PRIVACY)
        ]
        for section_name, locator in sections:
            assert page.element_is_visible(locator), f"Секция '{section_name}' не видна"
            logger.debug(f"Секция '{section_name}' видна")

        logger.success("Все секции футера отображаются корректно")

    def test_start_project_button(self, page):
        """Тест кнопки 'Начать проект' в футере"""
        logger.info("Проверка кнопки 'Начать проект'")

        # Проверка наличия кнопки
        assert page.element_is_present(self.LOCATOR.START_PROJECT_BUTTON), "Кнопка 'Начать проект' не найдена"

        # Проверка видимости
        assert page.element_is_visible(self.LOCATOR.START_PROJECT_BUTTON), "Кнопка 'Начать проект' не видна"

        # Проверка кликабельности
        assert page.element_is_clickable(
            self.LOCATOR.START_PROJECT_BUTTON), "Кнопка 'Начать проект' не кликабельна"

        # Проверка текста кнопки
        button = page.find_element(self.LOCATOR.START_PROJECT_BUTTON)
        button_text = button.text
        assert button_text, "Текст кнопки пуст"
        logger.debug(f"Текст кнопки: '{button_text}'")

        logger.success("Кнопка 'Начать проект' работает корректно")

    def test_footer_logo_functionality(self, page):
        """Тест функциональности логотипа в футере"""
        logger.info("Проверка логотипа в футере")

        # Проверка наличия логотипа
        assert page.element_is_present(self.LOCATOR.LOGO), "Логотип в футере не найден"

        # Проверка видимости
        assert page.element_is_visible(self.LOCATOR.LOGO), "Логотип в футере не виден"

        logger.success("Логотип в футере отображается корректно")

    def test_social_links_presence(self, page):
        """Тест наличия ссылок на социальные сети"""
        logger.info("Проверка ссылок на социальные сети")

        # Проверяем наличие контейнера соцсетей
        assert page.element_is_present(self.LOCATOR.SOCIALS), "Контейнер соцсетей не найден"

        # Находим все ссылки внутри контейнера соцсетей
        socials_container = page.find_element(self.LOCATOR.SOCIALS)
        social_links = socials_container.find_elements(By.TAG_NAME, 'a')

        # Проверяем, что есть хотя бы одна ссылка
        assert len(social_links) > 0, "Не найдено ссылок на социальные сети"

        logger.debug(f"Найдено {len(social_links)} ссылок на социальные сети")

        # Проверяем каждую ссылку
        for i, link in enumerate(social_links, 1):
            href = link.get_attribute('href')
            assert href, f"Ссылка #{i} не содержит URL"
            assert href.startswith('https'), f"Некорректный URL в ссылке #{i}: {href}"
            logger.debug(f"Ссылка #{i}: {href}")

        logger.success("Ссылки на социальные сети работают корректно")

    def test_privacy_policy_link(self, page):
        """Тест ссылки на политику конфиденциальности"""
        logger.info("Проверка ссылки на политику конфиденциальности")

        # Проверка наличия
        assert page.element_is_present(self.LOCATOR.PRIVACY), "Ссылка на политику конфиденциальности не найдена"

        # Проверка видимости
        assert page.element_is_visible(self.LOCATOR.PRIVACY), "Ссылка на политику конфиденциальности не видна"

        # Проверка текста
        privacy_link = page.find_element(self.LOCATOR.PRIVACY)
        link_text = privacy_link.text.strip()
        assert link_text, "Текст ссылки пуст"
        logger.debug(f"Текст ссылки: '{link_text}'")

        # Проверка URL
        href = privacy_link.get_attribute('href')
        assert href, "Ссылка не содержит URL"
        logger.debug(f"URL ссылки: {href}")

        # Проверка кликабельности
        assert page.element_is_clickable(
            self.LOCATOR.PRIVACY), "Ссылка на политику конфиденциальности не кликабельна"

        logger.success("Ссылка на политику конфиденциальности работает корректно")

    def test_footer_copyright_info(self, page):
        """Тест информации об авторских правах"""
        logger.info("Проверка информации об авторских правах")

        # Проверка года
        assert page.element_is_present(self.LOCATOR.YEAR), "Элемент с годом не найден"
        year_element = page.find_element(self.LOCATOR.YEAR)
        year_text = year_element.text.strip()
        assert year_text, "Текст с годом пуст"

        # Проверка, что текст содержит 2014 - 2025
        import re
        year_match = re.search(r'©\s*\d{4}\s*[-–—]\s*\d{4}', year_text)
        assert year_match, f"Текст '{year_text}' не соответсвуют паттерну: '©YYYY - YYYY'"
        logger.debug(f"Найдены годы: {year_match.group()}")

        # Проверка копирайтов
        assert page.element_is_present(self.LOCATOR.COPYRIGHTS), "Информация о копирайтах не найдена"

        logger.success("Информация об авторских правах отображается корректно")

    def test_footer_contact_info(self, page):
        """Тест контактной информации в футере"""
        logger.info("Проверка контактной информации")

        assert page.element_is_present(self.LOCATOR.CONTACT), "Контактная информация не найдена"

        # Находим все ссылки в контактах
        contact_container = page.find_element(self.LOCATOR.CONTACT)
        contact_links = contact_container.find_elements(By.TAG_NAME,'a')

        # Проверяем контактные ссылки
        for i, link in enumerate(contact_links, 1):
            href = link.get_attribute('href')
            link_text = link.text.strip()

            assert href, f"Контактная ссылка #{i} не содержит URL"
            assert link_text, f"Контактная ссылка #{i} не содержит текста"

            # Проверяем тип контакта
            if 'mailto:' in href:
                logger.debug(f"Email #{i}: {link_text} -> {href}")
            elif 'tel:' in href:
                logger.debug(f"Телефон #{i}: {link_text} -> {href}")
            else:
                logger.debug(f"Контакт #{i}: {link_text} -> {href}")

        logger.success("Контактная информация отображается корректно")

    def test_footer_scroll_behavior(self, page):
        """Тест поведения футера при скролле"""
        logger.info("Проверка поведения футера при скролле")

        # Прокручиваем в самый верх
        page.window_scroll('0', '0')
        # driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        # Футер должен быть скрыт или не в поле зрения
        initial_footer_position = page.find_element(self.LOCATOR.ROOT).location['y']

        # Прокручиваем вниз
        page.window_scroll('0', 'document.body.scrollHeight')
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # Футер должен быть видим
        footer = page.find_element(self.LOCATOR.ROOT)
        assert footer.is_displayed(), "Футер не виден после скролла вниз"

        logger.success("Футер корректно ведет себя при скролле")

    def test_footer_responsiveness(self, page, driver):
        """Тест адаптивности футера"""
        logger.info("Проверка адаптивности футера")

        # Тестируем разные разрешения
        resolutions = [
            (1920, 1080),  # Desktop
            (1366, 768),  # Laptop
            (768, 1024),  # Tablet
            (375, 667)  # Mobile
        ]

        for width, height in resolutions:
            driver.set_window_size(width, height)
            time.sleep(1)

            # Проверяем, что футер все еще присутствует
            assert page.element_is_present(self.LOCATOR.ROOT), f"Футер не найден при разрешении {width}x{height}"

            # Проверяем основные элементы
            assert page.element_is_visible(self.LOCATOR.SOCIALS), f"Соцсети не видны при {width}x{height}"
            assert page.element_is_visible(self.LOCATOR.CONTACT), f"Контакты не видны при {width}x{height}"
            assert page.element_is_visible(self.LOCATOR.PRIVACY), f"Политика конфиденциальности не видна при {width}x{height}"
            assert page.element_is_visible(self.LOCATOR.COPYRIGHTS), f"Копирайтер не виден при {width}x{height}"

            logger.debug(f"Футер корректно отображается при {width}x{height}")

        # Возвращаем исходный размер
        driver.set_window_size(1300, 1280)
        logger.success("Футер адаптивен на всех разрешениях")

class TestProjectsFooter(TestMainFooter):
    URL = 'https://only.digital/projects'

class TestCompanyFooter(TestMainFooter):
    URL = 'https://only.digital/company'

class TestFieldsFooter(TestMainFooter):
    URL = 'https://only.digital/fields'

class TestBlogFooter(TestMainFooter):
    URL = 'https://only.digital/blog'

class TestCareerFooter(TestMainFooter):  # не проходит, разобраться
    URL = 'https://only.digital/job'
    LOCATOR = AltFooterLocators
    def test_footer_sections_visibility(self, page):
        """Тест на видимость всех основных секций футера"""
        logger.info("Проверка видимости секций футера")

        sections = [
            #("Логотип", self.LOCATOR.LOGO),  # не используется для Карьера и Контакты
            ("Социальные сети", self.LOCATOR.SOCIALS),
            # ("Telegram секция", self.LOCATOR.TELEGRAM),  # не используется для Карьера и Контакты
            #("Контакты", self.LOCATOR.CONTACT),  # не используется для Карьера и Контакты
            #("Текст футера", self.LOCATOR.TEXT),  # не используется для Карьера и Контакты
            #("Презентация", self.LOCATOR.DOCUMENTS),  # не используется для Карьера и Контакты
            ("Годы", self.LOCATOR.YEAR),
            ("Копирайтер", self.LOCATOR.COPYRIGHTS),
            ("Политика конфиденциальности", self.LOCATOR.PRIVACY)
        ]
        for section_name, locator in sections:
            assert page.element_is_visible(locator), f"Секция '{section_name}' не видна"
            logger.debug(f"Секция '{section_name}' видна")

        logger.success("Все секции футера отображаются корректно")

    def test_start_project_button(self, page):
        logger.info("Проверка пропущена: функционал не используется для Карьера и Контакты")
        pytest.skip("Не используется")

    def test_footer_logo_functionality(self, page):
        logger.info("Проверка пропущена: функционал не используется для Карьера и Контакты")
        pytest.skip("Не используется")

    def test_footer_contact_info(self, page):
        logger.info("Проверка пропущена: функционал не используется для Карьера и Контакты")
        pytest.skip("Не используется")

    def test_footer_responsiveness(self, page, driver):
        """Тест адаптивности футера"""
        logger.info("Проверка адаптивности футера")

        # Тестируем разные разрешения
        resolutions = [
            (1920, 1080),  # Desktop
            (1366, 768),  # Laptop
            (768, 1024),  # Tablet
            (375, 667)  # Mobile
        ]

        for width, height in resolutions:
            driver.set_window_size(width, height)
            time.sleep(1)

            # Проверяем, что футер все еще присутствует
            assert page.element_is_present(self.LOCATOR.ROOT), f"Футер не найден при разрешении {width}x{height}"
            # Проверяем основные элементы
            assert page.element_is_visible(self.LOCATOR.SOCIALS), f"Соцсети не видны при {width}x{height}"
            # assert page.element_is_visible(self.LOCATOR.CONTACT), f"Контакты не видны при {width}x{height}" # не используется для Карьера и Контакты
            assert page.element_is_visible(
                self.LOCATOR.PRIVACY), f"Политика конфиденциальности не видна при {width}x{height}"
            assert page.element_is_visible(self.LOCATOR.COPYRIGHTS), f"Копирайтер не виден при {width}x{height}"

            logger.debug(f"Футер корректно отображается при {width}x{height}")

        # Возвращаем исходный размер
        driver.set_window_size(1300, 1280)
        logger.success("Футер адаптивен на всех разрешениях")

class TestContactsFooter(TestCareerFooter): # не проходит, разобраться
    URL = 'https://only.digital/contacts'