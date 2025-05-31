import allure
import requests

class KinopoiskApi:

    def __init__(self, base_url: str, token: str) -> None:
        """ конструктор вызывается при создании нового класса. Инициализирует объект класса и присваивает
            значения атрибутам объекта (base_url, token) """
        self.base_url = base_url
        self.token = token

    @allure.step('Отправить запрос GET на конечный URL с параметром: {keyword}')
    def get_film_by_keyword(self, keyword: str):
        """Метод предназначен для отправки HTTP-запроса GET к определённому API для поиска фильмов по ключевому слову.
                       :param keyword: str"""
        with allure.step("Сформировать конечный URL, используя {self.base_url}, добавленный путь запроса "
                         "и ключевое слово запроса {keyword}"):
            search_url = f"{self.base_url}v2.1/films/search-by-keyword?keyword={keyword}&page=1"
        with allure.step("Настроить заголовок запроса в формате JSON"):
            my_headers = {
                'Accept': 'application/json',
                'X-API-KEY': self.token,
            }

        result = requests.get(search_url, headers=my_headers)

        with allure.step("Вернуть результат ответа от сервера"):
            return result

    @allure.step('Отправить запрос GET на конечный URL с параметром: {film_id}')
    def get_film_by_id(self, film_id: str):
        """Метод предназначен для отправки HTTP-запроса GET к определённому API для поиска фильмов по id.
                               :param film_id: str"""
        with allure.step("Сформировать конечный URL, используя {self.base_url}, добавленный путь запроса "
                         "и ключевое слово запроса {film_id}"):
            search_url = f"{self.base_url}/v2.1/films/{film_id}"
        with allure.step("Настроить заголовок запроса в формате JSON"):
            my_headers = {
                'Accept': 'application/json',
                'X-API-KEY': self.token,
            }
        result = requests.get(search_url, headers=my_headers)
        with allure.step("Вернуть результат ответа от сервера"):
            return result

    @allure.step('Отправить запрос GET на конечный URL с параметрами: {year}, {month}')
    def get_premieres_film(self, year: int, month: str):
        """Метод предназначен для отправки HTTP-запроса GET к определённому API для поиска фильмов по id.
                                       :param month:
                                       :param year: int, month: str"""
        with allure.step("Сформировать конечный URL, используя {self.base_url}, добавленный путь запроса "
                         "и ключевое слово запроса {film_id}"):
            search_url = f"{self.base_url}v2.2/films/premieres"
        with allure.step("Настроить заголовок запроса в формате JSON"):
            my_headers = {
                'Accept': 'application/json',
                'X-API-KEY': self.token,
            }
        with allure.step("Настроить параметры запроса в формате JSON"):
            my_params = {
                'year': year,
                'month': month
            }
        result = requests.get(search_url, headers=my_headers, params=my_params)
        with allure.step("Вернуть результат ответа от сервера"):
            return result

    @allure.step('Отправить запрос GET на конечный URL для получения id жанров')
    def get_filters(self):
        """Метод предназначен для отправки HTTP-запроса GET к определённому API для поиска жанров фильмов."""
        with allure.step("Сформировать конечный URL, используя {self.base_url}, добавленный путь запроса "):
            search_url = f"{self.base_url}/v2.1/films/filters"
        with allure.step("Настроить заголовок запроса в формате JSON"):
            my_headers = {
                'Accept': 'application/json',
                'X-API-KEY': self.token,
            }
        result = requests.get(search_url, headers=my_headers)
        with allure.step("Вернуть результат ответа от сервера"):
            return result

    @allure.step('Отправить запрос GET на конечный URL для получения информации об искомом актере по {person_id}')
    def info_by_person_id(self, person_id:str):
        """Метод предназначен для отправки HTTP-запроса GET к определённому API для поиска
            информации об искомом актере, используя
            :param person_id: str"""
        with allure.step("Сформировать конечный URL, используя {self.base_url}, добавленный путь запроса и{person_id}"):
            search_url = f"{self.base_url}v1/staff/{person_id}"
        with allure.step("Настроить заголовок запроса в формате JSON"):
            my_headers = {
            'Accept': 'application/json',
            'X-API-KEY': self.token,
        }
        result = requests.get(search_url, headers=my_headers)
        with allure.step("Вернуть результат ответа от сервера"):
            return result

    @allure.step('Отправить запрос GET на конечный URL для получения информации об искомом актере по {name_actor}')
    def search_person(self, name_actor:str):
        """Метод предназначен для отправки HTTP-запроса GET к определённому API для поиска
                   информации об искомом актере, используя
                   :param name_actor: str"""
        with allure.step("Сформировать конечный URL, используя {self.base_url}, добавленный путь запроса и{name_actor}"):
            search_url = f"{self.base_url}v1/persons?name={name_actor}"
        with allure.step("Настроить заголовок запроса в формате JSON"):
            my_headers = {
                'Accept': 'application/json',
                'X-API-KEY': self.token,
            }
        result = requests.get(search_url,headers=my_headers)
        with allure.step("Вернуть результат ответа от сервера"):
            return result
