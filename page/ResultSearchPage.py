import  allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResultSearchPage:

    def __init__(self, driver: WebDriver) -> None:
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
                                       внутри экземпляра класса. """
        self.__driver = driver

    @allure.step('Получить со страницы текстовое значение количества найденных фильмов')
    def txt_search_result(self):
        """ Метод извлекает текстовое значение количества найденных фильмов на странице.
               Используетя механизм ожидания в 10 с. до появления элемента на странице.
               Результат выводится в терминал."""
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search_results_topText'))))
        txt = self.__driver.find_element(By.CSS_SELECTOR, '.search_results_topText')
        print(txt)
        return txt.text.strip()

    @allure.step('Получить количество найденных фильмов')
    def search_result(self) -> int:
        """ Метод извлекает список найденных фильмов со страницы из HTML-элемента.
        Возвращается список результатов."""
        result = self.__driver.find_elements(By.CSS_SELECTOR, ".element")
        return len(result)

    @allure.step('Выбрать фильм и кликнуть на него')
    def change_film(self) -> None:
        """Метод находит по локатору нужный фильм и кликает его"""
        self.__driver.find_element(By.CSS_SELECTOR, '[data-url="/film/5230101"]').click()

    @allure.step('Найти текущий URL')
    def get_current_url(self) -> str or None:
        """Возвращает текущий URL страницы"""
        return self.__driver.current_url
        print(f'Текущий URL: {current_url}')

