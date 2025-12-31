from selenium.webdriver.common.by import By

class MainPageLocators(object):
    HEADER_MENU = (By.CLASS_NAME, 'Header_links__CblPJ menu ')
    PROJECTS = (By.XPATH, '//a[contains(@class, "Header_link") and contains(text(), "Проекты")]')
    COMPANY = (By.XPATH, '//a[contains(@class, "Header_link") and contains(text(), "Компания")]')
    FIELDS = (By.XPATH, '//a[contains(@class, "Header_link") and contains(text(), "Направления")]')
    CAREER = (By.XPATH, '//a[contains(@class, "Header_link") and contains(text(), "Карьера")]')
    BLOG = (By.XPATH, '//a[contains(@class, "Header_link") and contains(text(), "Блог")]')
    CONTACTS = (By.XPATH, '//a[contains(@class, "Header_link") and contains(text(), "Контакты")]')


class FooterLocators(object):
    ROOT = (By.TAG_NAME, 'footer')
    START_PROJECT_BUTTON = (By.XPATH, '//div[@class="Footer_grid__lfZ34"]/button')
    LOGO = (By.CSS_SELECTOR, "svg.Footer_logo__2QEhf")
    SOCIALS = (By.XPATH, '//div[@class="Socials_socialsWrap__DPtp_ Footer_socials__C39yX"]')
    # list_socials = driver.find_element(By.XPATH, '//div[@class="Socials_socialsWrap__DPtp_ Footer_socials__C39yX"]').find_elements(By.TAG_NAME, 'a')
    # print([i.get_attribute('href') for i in list_socials])
    TELEGRAM = (By.XPATH, '//div[@class="Telegram_telegramWrap__USZkq Footer_telegram__Y0DSn"]')
    CONTACT = (By.XPATH, '//div[@class="ContactsLinks_contactLinks__vex86 Footer_contacts__s7c9v"]')
    TEXT = (By.XPATH, '//p[@class="text2 Footer_text___ATim"]')
    DOCUMENTS = (By.XPATH, '//div[@class="Documents_documentsWrap__iNfwU Footer_documents___mRvU"]')
    YEAR = (By.XPATH, '//p[@class="h4 Footer_year__nyNCc"]')
    COPYRIGHTS = (By.CSS_SELECTOR, 'div.copyrightsBig')
    PRIVACY = (By.XPATH, '//a[@class="text2 Footer_privacy__NdtU9"]')
