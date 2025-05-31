import  allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MoviePage:

    def __init__(self, driver: WebDriver) -> None:
        """ конструктор вызывается при создании нового класса. Принимает объект драйвера (браузера) и сохраняет его
                               внутри экземпляра класса. """
        self.__driver = driver

    @allure.step('Нажать на кнопку "Интернет-трейлер')
    def movie_treiler(self) -> None:
        """ ожидание появления элемента страницы по заданному локатору и клинкуть его """
        (WebDriverWait(self.__driver, 10).
         until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[href="/film/5230101/video/202093/"]')))).click()

    def get_current_url(self) -> str or None:
        """Возвращает текущий URL страницы"""
        return self.__driver.current_url
        print(f'Текущий URL: {current_url}')


