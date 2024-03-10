import allure

from litres_project.data.data import book
from litres_project.pages.ui.book_page import book_page


@allure.epic('Move book to/from favorites')
@allure.label("owner", "Devianochka")
@allure.feature("Checking whether a book has been added or removed from favorites")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_adding_book_to_favorites():
    book_page.open(book)
    book_page.adding_book_to_favorites()
    book_page.book_must_be_added_to_favorites(book)


@allure.epic('Move book to/from favorites')
@allure.label("owner", "Devianochka")
@allure.feature("Checking whether a book has been added or removed from favorites")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_removing_book_from_favorites():
    book_page.open(book)
    book_page.adding_book_to_favorites()
    book_page.removing_book_from_favorites()
    book_page.book_must_be_removed_from_favorites()
