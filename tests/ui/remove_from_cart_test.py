import allure

from litres_project.data.data import book
from litres_project.pages.ui.book_page import book_page
from litres_project.pages.ui.cart_page import cart_page


@allure.epic('Remove book from cart')
@allure.label("owner", "Devianochka")
@allure.feature("Checking whether a book has been removed from cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_removing_book_from_cart():
    book_page.open(book)
    book_page.adding_book_to_cart()
    cart_page.open()
    cart_page.removing_book_to_cart()
    cart_page.book_must_be_removed_from_cart()


@allure.epic('Remove book from cart')
@allure.label("owner", "Devianochka")
@allure.feature("Checking whether a book has been removed from cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'ui', 'normal')
@allure.severity('normal')
@allure.label('layer', 'ui')
def test_removing_book_from_cart_and_adding_to_favorites():
    book_page.open(book)
    book_page.adding_book_to_cart()
    cart_page.open()
    cart_page.removing_book_to_cart_and_adding_to_favorites()
    cart_page.book_must_be_removed_from_cart()
    book_page.book_must_be_added_to_favorites(book)
