import allure
import pytest

from config import api_films_url
from config import my_token
from api.KinopoiskApi import KinopoiskApi


api = KinopoiskApi(api_films_url, my_token)


@pytest.mark.api
@allure.severity('blocker')
@allure.title('Поиск фильма по ключевому слову')
@allure.story("API")
@allure.feature('Поиск фильма')
@allure.description('Поиск фильма по ключевому слову с помощью get-запроса на сервер')
def test_get_film_keyword():
    name_ru = "Огниво"
    film_list = api.get_film_by_keyword("огниво")
    films = film_list.json()['films']
    first_film = films[0]['nameRu']
    with allure.step("Проверить, что название первого фильма из списка найденных фильмов - 'Огниво'"):
        assert first_film == name_ru
    with allure.step("Проверить, cоответствует ли полученный код ответа HTTP запросу ожидаемому значению 200"):
        assert film_list.status_code == 200


@pytest.mark.api
@allure.severity('blocker')
@allure.title('Поиск фильма по id-фильма')
@allure.story("API")
@allure.feature('Поиск фильма')
@allure.description('Поиск фильма по id-фильма с помощью get-запроса на сервер')
def test_get_film_id():
    expected_film_id = 5230101
    result = api.get_film_by_id('5230101')
    actual_film_id = result.json()['data']['filmId']
    with allure.step("Проверить, что id найденного фильма соответствует id искомого"):
        assert actual_film_id == expected_film_id
    with allure.step("Проверить, cоответствует ли полученный код ответа HTTP запросу ожидаемому значению 200"):
        assert result.status_code == 200


@pytest.mark.api
@allure.severity('blocker')
@allure.title('Поиск кинопремьер')
@allure.story("API")
@allure.feature('Поиск фильма')
@allure.description('Поиск кинопремьер в определённый месяц года с помощью get-запроса на сервер')
def test_get_premieres_film():
    name_ru = "Волшебник Изумрудного города. Дорога из жёлтого кирпича"
    premieres_film_list = api.get_premieres_film(2025, "JANUARY")
    print(premieres_film_list.json())
    premieres = premieres_film_list.json()['items']
    first_premieres = premieres[0]['nameRu']
    with allure.step("Проверить, что название первого фильма из списка кинопремьер - "
                     "'Волшебник Изумрудного города. Дорога из жёлтого кирпича'"):
        assert first_premieres == name_ru
    with allure.step("Проверить, cоответствует ли полученный код ответа HTTP запросу ожидаемому значению 200"):
        assert premieres_film_list.status_code == 200


@pytest.mark.api
@allure.severity('blocker')
@allure.title('Поиск жанров фильмов')
@allure.story("API")
@allure.feature('Поиск жанра')
@allure.description('С помощью get-запроса на сервер получаем список жанров фильмов и id для каждого жанра')
def test_get_filters():
    expected_genre = 'мультфильм'
    expected_id = 14
    filters_list = api.get_filters()
    filters_genres = filters_list.json()['genres']
    mult = filters_genres[18]['genre']
    id_mult = filters_genres[18]['id']
    with allure.step("Проверить, cоответствует ли полученный код ответа HTTP запросу ожидаемому значению 200"):
        assert filters_list.status_code == 200
    with allure.step("Проверить, что 18 жанр в списке найденных жанров - мультфильм"):
        assert mult == expected_genre
    with allure.step("Проверить, что id найденного жанра - 14"):
        assert id_mult == expected_id


@pytest.mark.api
@allure.severity('blocker')
@allure.title('Поиск информации об актёре')
@allure.story("API")
@allure.feature('Поиск актёра')
@allure.description('С помощью get-запроса на сервер получаем индивидуальный id-актёра '
                    'и по нему получаем более подробную информацию об этом актёре')
def test_get_info_actor():
    expected_birthday = '1983-01-21'
    search_person = api.search_person('Светлана Ходченкова')
    result_s_p = search_person.json()['items']
    person_id = result_s_p[0]['kinopoiskId']

    info_actor = api.info_by_person_id(person_id)
    actual_birthday = info_actor.json()['birthday']
    with allure.step("Проверить, что дата рождения искомого актера в ответе запроса соответствует ожидаемой"):
        assert actual_birthday == expected_birthday
    with allure.step("Проверить, cоответствует ли полученный код ответа HTTP запросу ожидаемому значению 200"):
        assert info_actor.status_code == 200
