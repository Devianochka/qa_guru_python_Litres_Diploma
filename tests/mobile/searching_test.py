import allure

from litres_project.pages.mobile.books_to_read_page import book_search_page
from litres_project.pages.mobile.main_page import main_page


@allure.epic('Search')
@allure.label("owner", "Devianochka")
@allure.feature("Checking the book search in mobile app")
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_successful_searching_book():
    main_page.selecting_application_language()
    main_page.hiding_adult_content()

    book_search_page.searching_book()

    book_search_page.book_must_be_found()


@allure.epic('Search')
@allure.label("owner", "Devianochka")
@allure.feature("Checking the book search in mobile app")
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_unsuccessful_searching_book():
    main_page.selecting_application_language()
    main_page.hiding_adult_content()

    book_search_page.searching_non_existent_book()

    book_search_page.book_must_not_be_found()
