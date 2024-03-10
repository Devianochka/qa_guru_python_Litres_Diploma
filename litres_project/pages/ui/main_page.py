from selene import browser, be, have
import allure

class MainPage:
    def open(self):
        with allure.step("Open the book page"):
            browser.open("")
            return self

    def filling_authorization_form(self, user):
        with allure.step("Open the book page"):
            browser.element('[href="/pages/login/"]').should(be.visible).click()
            browser.element('[name="email"]').should(be.visible).type(user.email)
            browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()
            browser.element('[name="pwd"]').should(be.visible).type(user.password)
            browser.element('.AuthContent-module__form__submit_jot-u > [type="submit"]').should(be.visible).click()
        return self

    def user_must_be_authorized(self, user):
        with allure.step("Checking that user has been authorized"):
            browser.element('.ProfileButton-module__profileButton_2ajQV').should(be.visible).click()
            browser.open("pages/personal_cabinet_about_me/")
            browser.element('span[class="user_header__name"]').should(have.text(user.name))
        return self

    def user_must_not_be_authorized(self):
        with allure.step("Checking that user has not been authorized"):
            browser.element('.ControlInput-module__input__error_2jXOB').should(have.text('Неверное сочетание логина и '
                                                                                         'пароля'))
        return self

    def search_book_by_title(self, book):
        with allure.step("Enter the name of the book in the search and click the Find button"):
            browser.element('[data-testid="header__search-input--desktop"]').should(be.visible).type(book.name)
            browser.element('[data-testid="header__search-button--desktop"]').should(be.visible).click()

        return self

    def book_with_specified_title_must_be_found(self):
        with allure.step("Checking that books with the specified title are found in the search"):
            browser.element('[data-testid="art__title"]').should(have.text('Стоя под радугой'))

        return self

    def search_book_by_author(self, book):
        with allure.step("Enter the author of the book in the search and click the Find button"):
            browser.element('[data-testid="header__search-input--desktop"]').should(be.visible).type(book.author)
            browser.element('[data-testid="header__search-button--desktop"]').should(be.visible).click()
        return self

    def book_with_specified_author_must_be_found(self, book):
        with allure.step("Checking that books with the specified title are found in the search"):
            browser.element('[data-testid="art__authorName"]').should(have.text(book.author))
        return self


main_page = MainPage()
