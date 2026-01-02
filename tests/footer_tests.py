import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.locators import MainPageLocators as main_loc
from utils.locators import FooterLocators as foot_loc
from pages.home_page import HomePage
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


@pytest.fixture(scope='class')
def home_page(driver):
    """Фикстура для домашней страницы (загружается один раз)"""
    from pages.home_page import HomePage

    page = HomePage(driver, 'https://only.digital/')
    page.open()
    logger.info("Страница загружена")
    page.scroll_to_element(foot_loc.ROOT)
    logger.info("Скролл до футера выполнен")
    return page


class TestFooter:

    def test_footer_presence(self, home_page):
        """Тест на наличие футера на странице"""
        logger.info("Проверка наличия футера на странице")
        assert home_page.is_footer_present(), "Футер не найден на странице"
        # Проверка, что футер видим
        assert home_page.is_footer_visible(), "Футер не видим на странице"
        logger.success("Футер успешно найден и видим")

    def test_footer_sections_visibility(self, home_page):
        """Тест на видимость всех основных секций футера"""
        logger.info("Проверка видимости секций футера")

        sections = [
            ("Логотип", foot_loc.LOGO),
            ("Социальные сети", foot_loc.SOCIALS),
            ("Telegram секция", foot_loc.TELEGRAM),
            ("Контакты", foot_loc.CONTACT),
            ("Текст футера", foot_loc.TEXT),
            ("Презентация", foot_loc.DOCUMENTS),
            ("Годы", foot_loc.YEAR),
            ("Копирайтер", foot_loc.COPYRIGHTS),
            ("Политика конфиденциальности", foot_loc.PRIVACY)
        ]
        for section_name, locator in sections:
            assert home_page.is_element_visible(locator), f"Секция '{section_name}' не видна"
            logger.debug(f"Секция '{section_name}' видна")

        logger.success("Все секции футера отображаются корректно")

    def test_start_project_button(self, home_page):
        """Тест кнопки 'Начать проект' в футере"""
        logger.info("Проверка кнопки 'Начать проект'")

        # Проверка наличия кнопки
        assert home_page.is_element_present(foot_loc.START_PROJECT_BUTTON), "Кнопка 'Начать проект' не найдена"

        # Проверка видимости
        assert home_page.is_element_visible(foot_loc.START_PROJECT_BUTTON), "Кнопка 'Начать проект' не видна"

        # Проверка кликабельности
        assert home_page.is_element_clickable(
            foot_loc.START_PROJECT_BUTTON), "Кнопка 'Начать проект' не кликабельна"

        # Проверка текста кнопки
        button = home_page.find_element(foot_loc.START_PROJECT_BUTTON)
        button_text = button.text
        assert button_text, "Текст кнопки пуст"
        logger.debug(f"Текст кнопки: '{button_text}'")

        logger.success("Кнопка 'Начать проект' работает корректно")

    def test_footer_logo_functionality(self, home_page):
        """Тест функциональности логотипа в футере"""
        logger.info("Проверка логотипа в футере")

        # Проверка наличия логотипа
        assert home_page.is_element_present(foot_loc.LOGO), "Логотип в футере не найден"

        # Проверка видимости
        assert home_page.is_element_visible(foot_loc.LOGO), "Логотип в футере не виден"

        logger.success("Логотип в футере отображается корректно")

    def test_social_links_presence(self, home_page):
        """Тест наличия ссылок на социальные сети"""
        logger.info("Проверка ссылок на социальные сети")

        # Проверяем наличие контейнера соцсетей
        assert home_page.is_element_present(foot_loc.SOCIALS), "Контейнер соцсетей не найден"

        # Находим все ссылки внутри контейнера соцсетей
        socials_container = home_page.find_element(foot_loc.SOCIALS)
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

    def test_privacy_policy_link(self, home_page):
        """Тест ссылки на политику конфиденциальности"""
        logger.info("Проверка ссылки на политику конфиденциальности")

        # Проверка наличия
        assert home_page.is_element_present(foot_loc.PRIVACY), "Ссылка на политику конфиденциальности не найдена"

        # Проверка видимости
        assert home_page.is_element_visible(foot_loc.PRIVACY), "Ссылка на политику конфиденциальности не видна"

        # Проверка текста
        privacy_link = home_page.find_element(foot_loc.PRIVACY)
        link_text = privacy_link.text.strip()
        assert link_text, "Текст ссылки пуст"
        logger.debug(f"Текст ссылки: '{link_text}'")

        # Проверка URL
        href = privacy_link.get_attribute('href')
        assert href, "Ссылка не содержит URL"
        logger.debug(f"URL ссылки: {href}")

        # Проверка кликабельности
        assert home_page.is_element_clickable(
            foot_loc.PRIVACY), "Ссылка на политику конфиденциальности не кликабельна"

        logger.success("Ссылка на политику конфиденциальности работает корректно")

    def test_footer_copyright_info(self, home_page):
        """Тест информации об авторских правах"""
        logger.info("Проверка информации об авторских правах")

        # Проверка года
        assert home_page.is_element_present(foot_loc.YEAR), "Элемент с годом не найден"
        year_element = home_page.find_element(foot_loc.YEAR)
        year_text = year_element.text.strip()
        assert year_text, "Текст с годом пуст"

        # Проверка, что текст содержит 2014 - 2025
        import re
        year_match = re.search(r'©\s*\d{4}\s*[-–—]\s*\d{4}', year_text)
        assert year_match, f"Текст '{year_text}' не соответсвуют паттерну: '''©\s*\d{4}\s*[-–—]\s*\d{4}'''"
        logger.debug(f"Найден год: {year_match.group()}")

        # Проверка копирайтов
        assert home_page.is_element_present(foot_loc.COPYRIGHTS), "Информация о копирайтах не найдена"

        logger.success("Информация об авторских правах отображается корректно")

    def test_footer_contact_info(self, home_page):
        """Тест контактной информации в футере"""
        logger.info("Проверка контактной информации")

        assert home_page.is_element_present(foot_loc.CONTACT), "Контактная информация не найдена"

        # Находим все ссылки в контактах
        contact_container = home_page.find_element(foot_loc.CONTACT)
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

    def test_footer_scroll_behavior(self, home_page, driver):
        """Тест поведения футера при скролле"""
        logger.info("Проверка поведения футера при скролле")

        # Прокручиваем в самый верх
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        # Футер должен быть скрыт или не в поле зрения
        initial_footer_position = home_page.find_element(foot_loc.ROOT).location['y']

        # Прокручиваем вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        # Футер должен быть видим
        footer = home_page.find_element(foot_loc.ROOT)
        assert footer.is_displayed(), "Футер не виден после скролла вниз"

        logger.success("Футер корректно ведет себя при скролле")

    def test_footer_responsiveness(self, home_page, driver):
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
            assert home_page.is_footer_present(), f"Футер не найден при разрешении {width}x{height}"

            # Проверяем основные элементы
            assert home_page.is_element_visible(foot_loc.SOCIALS), f"Соцсети не видны при {width}x{height}"
            assert home_page.is_element_visible(foot_loc.CONTACT), f"Контакты не видны при {width}x{height}"
            assert home_page.is_element_visible(foot_loc.PRIVACY), f"Политика конфиденциальности не видна при {width}x{height}"
            assert home_page.is_element_visible(foot_loc.COPYRIGHTS), f"Копирайтер не виден при {width}x{height}"

            logger.debug(f"Футер корректно отображается при {width}x{height}")

        # Возвращаем исходный размер
        driver.set_window_size(1300, 1280)
        logger.success("Футер адаптивен на всех разрешениях")