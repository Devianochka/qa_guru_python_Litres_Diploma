import allure
from selene import browser, have
from appium.webdriver.common.appiumby import AppiumBy


class AndroidSearchBookPage:

    def searching_book(self):
        with allure.step('Type search'):
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/search")).click()
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/et_search_query")).type('The adventures of Tom Sawyer')
        return self

    def book_must_be_found(self):
        with allure.step('Verify content found'):
            results = browser.all((AppiumBy.ID, 'ru.litres.android.global:id/searchList'))
            results.should(have.size_greater_than(0))
            (browser.element((AppiumBy.ID, "ru.litres.android.global:id/bookName")).should(have.text('The Adventures of Tom Sawyer')))
        return self

    def searching_non_existent_book(self):
        with allure.step('Type search'):
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/search")).click()
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/et_search_query")).type('sdflksd')
        return self

    def book_must_not_be_found(self):
        with allure.step('Verify content not found'):
            results = browser.all((AppiumBy.ID, 'ru.litres.android.global:id/empty_view'))
            results.should(have.size(1))
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/title")).should(have.text('Nothing found'))
            (browser.element((AppiumBy.ID, "ru.litres.android.global:id/tv_books_search_empty_message"))
             .should(have.text('Make sure you entered the search query correctly')))
        return self

    def choosing_book(self):
        with allure.step('Choosing a book'):
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/bookName")).click()
        return self


book_search_page = AndroidSearchBookPage()
