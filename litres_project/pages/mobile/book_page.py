import allure
from selene import browser, have, be
from appium.webdriver.common.appiumby import AppiumBy


class AndroidBookPage:

    def adding_book_to_saved(self):
        with allure.step('Adding a book to Saved'):
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/bookPostpone")).click()
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/textViewBookSectionTitle")).click()
        return self

    def go_to_saved_tab(self):
        with allure.step('Go to the Saved tab'):
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/nav_my_audiobooks")).click()
            browser.element((AppiumBy.ACCESSIBILITY_ID, "SAVED")).click()
        return self

    def book_must_be_added_to_saved(self):
        with allure.step('Checking that the selected book has been added to Saved'):
            (browser.element((AppiumBy.ID, "ru.litres.android.global:id/bookName"))
             .should(have.text("The Adventures of Tom Sawyer")))
        return self

    def removing_book_from_saved(self):
        with allure.step('Removing a book from Saved'):
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/bookName")).click()
            browser.element((AppiumBy.ID, "ru.litres.android.global:id/bookPostpone")).click()
        return self

    def book_must_be_removed_from_saved(self):
        with allure.step('Checking that the selected book has been removed from Saved'):
            results = browser.all((AppiumBy.ID, 'ru.litres.android.global:id/empty_view'))
            results.should(have.size(1))
            browser.element((AppiumBy.ID, 'ru.litres.android.global:id/action_button')).should(be.visible)
        return self


book_page = AndroidBookPage()
