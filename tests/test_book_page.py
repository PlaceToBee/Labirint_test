from pages.book_page import BookPage


def test_open_book(web_browser):
    """Тестирование открытия книги на главной странице."""
    page = BookPage(web_browser)
    page.book.click()

    assert page.book_info


def test_buy_book(web_browser):
    """Добавление книги в корзину."""
    page = BookPage(web_browser)
    page.book.click()
    page.buy_book.click()

    assert page.message_buy_book


def test_deferred_books(web_browser):
    """Добавление книги в 'Отложенные'."""
    page = BookPage(web_browser)
    page.book.click()
    page.deferred_books.click()

    assert page.message_deferred_books


def test_book_comparison(web_browser):
    """Добавление книги 'К сравнению'"""
    page = BookPage(web_browser)
    page.book.click()
    page.comparison_book_page.click()
    page.comparison_book.clikc()

    assert page.message_comparison_book
