# Diplom_Kinopoisk

## Описание
Финальная работа по ручному тестированию: <https://culia7748.atlassian.net/wiki/spaces/pNLQWMkG1PdH/pages/54394881>

**Сайт:** <www.kinopoisk.ru>

**Продукт:** Кинопоиск

**Описание продукта:** Интернет-сервис “КиноПоиск” - один из крупнейших онлайн-кинотеатров в России.<br> 
Помимо просмотра фильмов, сервис предоставляет информацию о кинофильмах, телесериалах.<br>
В том числе предоставляет кадры, трейлеры, постеры, обои, а также данные о персонах, <br>
связанных с кино- и телепроизводством: актёрах, режиссёрах, продюсерах, сценаристах, операторах, композиторах, <br>
художниках и монтажёрах. Посетители могут ставить оценки фильмам и сериалам, добавлять их в ожидаемые, <br>
писать рецензии, покупать билеты в кинотеатры на сайте с компьютера или мобильных устройств. <br>
Имеется онлайн-кинотеатр с фильмами и сериалами по подписке «Яндекс. Плюс» или за отдельную плату. <br>
Приложение «Кинопоиск» можно устанавливать на Android и iOS, Apple TV, <br>
Smart TV (LG, Samsung и телевизоры на базе Android TV), игровые консоли PlayStation 4 и PlayStation 5.

**API-документация:** <https://kinopoiskapiunofficial.tech/documentation/api/#/>

## Структура

api - класс для api-тестирования

+ `KinopoiskApi.py`

pages - классы для ui-тестирования
    
+ `AuthPage.py`
+ `MainPage.py`
+ `MoviePage.py`
+ `ResultSearchPage.py`

tests - тесты

+ `tests/test_API.py`
+ `tests/test_UI.py`

`pytest.ini` - маркеры для запуска pytest

`README.md` - отчет-инструкция к работе

`config.py` - конфигурации

`requirements.txt` - зависимости


### Инструкция по работе с тестами

1. Склонировать проект `git clone https://github.com/имя_пользователя/
   pytest_ui_api_template.git`
2. Установить все зависимости `pip instal -r requirements.txt`
3. Запустить тесты 'pytest -s -v'
    + Запустить только ui тесты "pytest -m ui"
    + Запустить только api тесты "pytest -m api"
    + Запустить ui и api тесты 'pytest -m api or ui'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- **pytest** - основная библиотека для написания и выполнения тестов.
- **selenium** - библиотека для автоматизации UI тестирования.
- **webdriver manager** - библиотека для автоматической установки драйверов.
- **requests** - библиотека для работы с HTTP-клиентом, используемая для API тестирования.
- **allure** - библиотека для генерации отчетов о выполнении тестов.

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)

### Команды для установки библиотек
- pyp install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest