from selene import browser, be, have
import allure

class BookPage:
    def open(self, book):
        with allure.step("Open the main page"):
            browser.open(f"book/{book.url}")
        return self

    def adding_book_to_cart(self):
        with allure.step("Adding the selected book to the cart"):
            browser.element('[data-testid="book__addToCartButton--desktop"]').should(be.visible).click()
            browser.driver.refresh()
        return self

    def book_must_be_added_to_cart(self, book):
        with allure.step("Checking that the book has been added to the cart"):
            browser.open("my-books/cart/")
            browser.element('[data-testid="cart__bookCardTitle--wrapper"]').should(have.text(book.name))
            browser.element('[data-testid="cart__bookCardAuthor--wrapper"]').should(have.text(book.author))
            browser.element('[data-testid="cart__bookCardDiscount--wrapper"]').should(have.text(book.price))
        return self

    def adding_books_to_cart(self):
        with allure.step("Adding the selected book to the cart"):
            browser.element('[data-testid="book__addToCartButton--desktop"]').should(be.visible).click()
            browser.driver.refresh()
        return self

    def books_must_be_added_to_cart(self, book, book2):
        with allure.step("Checking that the books has been added to the cart"):
            browser.open("my-books/cart/")
            browser.element(f'h3 > a[href="/book/{book.url}"]').should(have.text(book.name))
            browser.element('div:nth-child(1) > div.Cart-module__bookCard__author_20vL8').should(have.text(book.author))
            browser.element('div:nth-child(1) > div.Cart-module__bookCard__price_336CO').should(have.text(book.price))
            browser.element(f'h3 > a[href="/book/{book2.url}"]').should(have.text(book2.name))
            browser.element('div:nth-child(2) > div.Cart-module__bookCard__author_20vL8').should(have.text(book2.author))
            browser.element('div:nth-child(2) > div.Cart-module__bookCard__price_336CO').should(have.text(book2.price))
        return self

    def adding_book_to_favorites(self):
        with allure.step("Adding a book to favorites"):
            browser.element('ul > li:nth-child(2) > button > div').should(be.visible).click()
        return self

    def book_must_be_added_to_favorites(self, book):
        with allure.step("Checking that the book has been added to favorites"):
            browser.open("my-books/liked/")
            browser.element('[data-testid="art__title"]').should(have.text(book.name))
            browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
        return self

    def removing_book_from_favorites(self):
        with allure.step("Removing a book to favorites"):
            browser.open("my-books/liked/")
            browser.element('div.ArtV2Default-module__like_button_1VLId > div').should(be.visible).click()
            browser.element('//*[@id=":r4:"]/div/div/div[3]').should(be.visible).click()
        return self

    def book_must_be_removed_from_favorites(self):
        with allure.step("Checking that the book has been removed from favorites"):
            browser.element('.EmptyState-module__empty__content_2lpJ-').should(have.text('Здесь будет все, что вы '
                                                                                         'отложите на потом'))
        return self


book_page = BookPage()
