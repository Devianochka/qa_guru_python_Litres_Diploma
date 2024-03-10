import allure

from litres_project.data.data import book
from litres_project.pages.ui.main_page import main_page


@allure.epic('Search')
@allure.label("owner", "Devianochka")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_searching_of_book_by_title():
    main_page.open()
    main_page.search_book_by_title(book)
    main_page.book_with_specified_title_must_be_found()


@allure.epic('Search')
@allure.label("owner", "Devianochka")
@allure.feature("Checking the book search on the main page")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_searching_of_book_by_author():
    main_page.open()
    main_page.search_book_by_author(book)
    main_page.book_with_specified_author_must_be_found(book)
