import allure
import pytest
from page.AuthPage import AuthPage
from page.MainPage import MainPage
from page.MoviePage import MoviePage
from page.ResultSearchPage import ResultSearchPage
from conftest import browser


@pytest.mark.ui
@allure.severity('blocker')
@allure.title('Поиск фильма через поисковую строку')
@allure.story('UI')
@allure.feature('Поиск')
@allure.description('Поиск фильма по названию через поисковую строку на главной странице')
def test_search_film(browser):
    auth_page = AuthPage(browser)
    auth_page.go()

    main_page = MainPage(browser)
    main_page.search_film("Огниво")
    main_page.search_button()

    result_search_page = ResultSearchPage(browser)
    txt = result_search_page.txt_search_result()
    actual_txt = txt
    results = result_search_page.search_result()
    with allure.step("Сравнение ожидаемого количества найденных фильмов ({expected_count}) с фактическим "
                     "результатом ({results}) на первой странице"):
        expected_count = 6  # Ожидаемое количество результатов
        assert results == expected_count, (f"Количество результатов поиска отличается! Получено: {results}, "
                                           f"ожидаемое: {expected_count}")
    with allure.step("Проверка соответствия текста результатов поиска"):
        expected_text = f"поиск: Огниво • результаты: 12"  # Текстовая информация, соответствующая количеству
        assert actual_txt == expected_text, (f"Текст результата поиска неверен! Получено: '{actual_txt}',"
                                             f" ожидается: '{expected_text}'")


@pytest.mark.ui
@allure.severity('blocker')
@allure.title('Переход на страницу фильма при выборе его из списка фильмов')
@allure.story('UI')
@allure.feature('Страница фильма')
@allure.description('Возможность перейти на страницу фильма при нажатии на название фильма в списке фильмов')
def test_change_film(browser):
    auth_page = AuthPage(browser)
    auth_page.go()

    main_page = MainPage(browser)
    main_page.search_film("Огниво")
    main_page.search_button()

    result_search_page = ResultSearchPage(browser)
    result_search_page.change_film()

    current_url = result_search_page.get_current_url()
    with allure.step("Сравнение ожидаемого URL-адреса страницы информации о фильме с фактическим"):
        assert current_url == "https://www.kinopoisk.ru/film/5230101/"


@pytest.mark.ui
@allure.severity('blocker')
@allure.title('Кликабельность кнопки "Войти"')
@allure.story('UI')
@allure.feature('Кнопка "Войти"')
@allure.description('При нажатии на кнопку "Войти" на главной странице сайта, '
                    'страница переходит на страницу авторизации')
def test_button_entrance(browser):
    """Ожидаемое название поля ввода"""
    expected_text = "Введите номер телефона"

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.entrance_button()
    actual_text = auth_page.find_element_auth()

    with allure.step("Проверить соответствие ожидаемого названия поля с фактическим"):
        if not actual_text == expected_text:
            raise AssertionError(
                f"Текст логотипа отличается! Ожидаемый: '{expected_text}', Фактический: '{actual_text}'"
                )
        else:
            print(f"Успешно найдено: {actual_text}")


@pytest.mark.ui
@allure.severity('blocker')
@allure.title('Кликабельность кнопки "Интернет-трейлер"')
@allure.story('UI')
@allure.feature('Кнопка "Интернет-трейлер"')
@allure.description('При нажатии на кнопку "Интернет-трейлер" на странице информации о фильме,'
                    'страница переходит на страницу просмотра трейлера фильма')
def test_movie_treiler(browser):
    auth_page = AuthPage(browser)
    auth_page.go()

    main_page = MainPage(browser)
    main_page.search_film("Огниво")
    main_page.search_button()

    result_search_page = ResultSearchPage(browser)
    result_search_page.change_film()

    movie_page = MoviePage(browser)
    movie_page.movie_treiler()

    with allure.step("Проверить соответствие ожидаемого URL страницы с фактическим"):
        movie_current_url = movie_page.get_current_url()
        assert  movie_current_url == "https://www.kinopoisk.ru/film/5230101/video/202093/"


@pytest.mark.ui
@allure.severity('blocker')
@allure.title('Кликабельность кнопки "Расширенный поиск"')
@allure.story('UI')
@allure.feature('Кнопка "Расширенный поиск"')
@allure.description('При нажатии на кнопку "Расширенный поиск" на главной странице в правой стороне поисковой строки,'
                    'страница переходит на страницу поиска фильма с фильтрами')
def test_search_main(browser):
    auth_page = AuthPage(browser)
    auth_page.go()

    main_page = MainPage(browser)
    main_page.button_search_page()

    with allure.step("Проверить соответствие ожидаемого URL страницы с фактическим"):
        search_main_url = main_page.get_current_url()
        assert search_main_url == "https://www.kinopoisk.ru/s/"
