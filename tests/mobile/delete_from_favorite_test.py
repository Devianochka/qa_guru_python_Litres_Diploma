import allure

from litres_project.pages.mobile.book_page import book_page
from litres_project.pages.mobile.books_to_read_page import book_search_page
from litres_project.pages.mobile.main_page import main_page


@allure.epic('Remove book to saved')
@allure.label("owner", "Devianochka")
@allure.feature("Checking whether a book has been removed from saved in mobile app")
@allure.severity('normal')
@allure.label('layer', 'mobile')
def test_removing_book_to_saved():
    main_page.selecting_application_language()
    main_page.hiding_adult_content()

    book_search_page.searching_book()
    book_search_page.choosing_book()
    book_page.adding_book_to_saved()

    book_page.go_to_saved_tab()
    book_page.removing_book_from_saved()
    book_page.go_to_saved_tab()
    book_page.book_must_be_removed_from_saved()
