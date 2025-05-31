import  allure
from config import ui_url
from selenium import webdriver
from selenium.webdriver.common.by import By
from  allure_commons.types import AttachmentType
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:

    def __init__(self, driver: webdriver) -> None:
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
                                                     внутри экземпляра класса. """
        self.__url = ui_url
        self.__driver = driver

    @allure.step("Перейти на главную страницу сайта Кинопоиск")
    def go(self) -> None:
        """Метод осуществляет переход на страницу сайта по заданному URL"""
        self.__driver.get(self.__url)

    @allure.step('Нажать на кнопку "Войти" на главной странице сайта')
    def entrance_button(self) -> None:
        """Метод находит по локатору поле кнопку "Войти" и кликает её."""
        self.__driver.find_element(By.CSS_SELECTOR, ".styles_loginButton__LWZQp").click()

    @allure.step('Получить текстовое значение названия поля ввода на странице авторизации')
    def find_element_auth(self) -> str:
        """Метод извлекает название поля ввода со страницы.
               Используетя механизм ожидания в 10 с. до появления элемента на странице.
               Возвращается фактическое строковое значение названия поля."""
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.passp-auth-content'))))
        logo_element = self.__driver.find_element(By.CSS_SELECTOR, ".passp-add-account-page-title")
        actual_text = logo_element.text.strip()
        return actual_text



    def number_input(self, number) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, "#passp-field-phone").send_keys(number)

    def entrance_button_two(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, ".Button2_view_contrast-action").click()

    def phone_code(self, code) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, "#passp-field-phoneCode").send_keys(code)

    def further_button(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, ".Button2_view_contrast-action.Button2_width_max").click()

    def account(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, ".AccountsListItem-account").click()

    def open_menu(self) -> None:
        self.__driver.find_element(By.CSS_SELECTOR, ".styles_root__42Fk8").click()

    def get_account_info(self) -> list[str]:
        txt = self.__driver.find_element(By.CSS_SELECTOR,
                                               "span.Text.Text_typography_primary.UserId-FirstLine").text
        print(txt)
