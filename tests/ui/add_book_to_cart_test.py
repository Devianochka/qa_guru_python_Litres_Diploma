import allure

from litres_project.data.data import book, book2
from litres_project.pages.ui.book_page import book_page


@allure.epic('Add book to cart')
@allure.label("owner", "Devianochka")
@allure.feature("Checking whether a book has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_adding_book_to_cart():
    book_page.open(book)
    book_page.adding_book_to_cart()
    book_page.book_must_be_added_to_cart(book)


@allure.epic('Add book to cart')
@allure.label("owner", "Devianochka")
@allure.feature("Checking whether a books has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_adding_books_to_cart():
    book_page.open(book)
    book_page.adding_book_to_cart()
    book_page.open(book2)
    book_page.adding_book_to_cart()
    book_page.books_must_be_added_to_cart(book, book2)
