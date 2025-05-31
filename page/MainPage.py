import  allure
from config import ui_url
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
                                              внутри экземпляра класса. """
        self.__url = ui_url
        self.__driver = driver

    @allure.step('Ввести в  поисковую строку название фильма: название {input}')
    def search_film(self, input: str) -> None:
        """Метод находит по локатору поле поисковой строки. Вводит заданное название фильма
               :param input: str"""
        search_input = (self.__driver.find_element(By.CSS_SELECTOR,
                    '.styles_inputActive__ICcod').send_keys(input))

    @allure.step('Нажать на кнопку поиска (значок лупы в правой стороне поисковой строки)')
    def search_button(self) -> None:
        """Метод находит по локатору кнопку вызова поиска и кликает её"""
        search_button = self.__driver.find_element(By.CSS_SELECTOR,".search-form-submit-button__icon").click()

    @allure.step('Нажать на кнопку расширенного поиска (значок бегунков в правой стороне поисковой строки)')
    def button_search_page(self) -> None:
        """Метод находит по локатору кнопку вызова расширенного поиска и кликает её"""
        button_search_page = self.__driver.find_element(By.CSS_SELECTOR,
                                   ".styles_advancedSearchIconActive__4bcK9.styles_advancedSearchIcon__Zxjax")
        button_search_page.click()

    @allure.step('Найти текущий URL')
    def get_current_url(self) -> str or None:
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#formSearchMain'))))
        """Возвращает текущий URL страницы"""
        return self.__driver.current_url
        print(f'Текущий URL: {current_url}')


    # @allure.step("Получить текущий URL")
    # def get_current_url(self) -> str:
    #     return self.__driver.current_url

    # @allure.step("Открыть боковое меню")# Нажимаем на иконку с именем в верхнем правом углу:
    # def open_menu(self):
    #     self.__driver.find_element(By.CSS_SELECTOR,
    #                                '[data-testid="header-member-menu-avatar"]').click()
    #
    # @allure.step("Получить информацию о пользователе")
    # def get_account_info(self) -> list[str]:
    #     # Ожидаем полной загрузки меню
    #     (WebDriverWait(self.__driver, 10).
    #      until(EC.visibility_of_element_located((By.CSS_SELECTOR,
    #                                              '[data-testid="account-menu-account-section"]'))))
    #     container = self.__driver.find_element(By.CSS_SELECTOR,
    #                                            '[data-testid="account-menu-account-section"]>div>div:last-child')
    #     fields = container.find_elements(By.CSS_SELECTOR, 'div')
    #     name = fields[0].text
    #     email = fields[1].text
    #     # Возвращаем имя и почту пользователя:
    #     return [name, email]