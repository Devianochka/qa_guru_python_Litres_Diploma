from selene import browser, be, have
import allure


class CartPage:
    def open(self):
        with allure.step("Open the cart page"):
            browser.open('my-books/cart/')
        return self

    def removing_book_to_cart(self):
        with allure.step("Removing the selected book from cart"):
            browser.element('[data-testid="cart__listDeleteButton--desktop"]').should(be.visible).click()
            browser.element('.Modal-module__controls_1qN-h > .Button-module__button_primary_2FaKg').should(
            be.visible).click()
        return self

    def book_must_be_removed_from_cart(self):
        with allure.step("Checking that the book has been removed from cart"):
            browser.element('.EmptyState-module__empty__title_22qdT').should(have.text('Корзина пуста'))
        return self

    def removing_book_to_cart_and_adding_to_favorites(self):
        with allure.step("Removing the selected book from cart and adding book to favorites"):
            browser.element('[data-testid="cart__listDeleteButton--desktop"] > div').should(be.visible).click()
            browser.element('.Button-module__button_secondary_2G8Ew').should(be.visible).click()
        return self


cart_page = CartPage()
