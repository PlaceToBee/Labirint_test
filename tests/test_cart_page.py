from pages.cart_page import CartPage


def test_book_add_to_cart(web_browser):
    """Тестирование добавления книги в корзину."""
    page = CartPage(web_browser)
    page.book.click()
    page.buy_book.click()

    assert page.message_buy_book


def test_cart_page_remove(web_browser):
    """Тестирование очистки корзины."""
    page = CartPage(web_browser)
    page.book.click()
    page.buy_book.click()
    page.button_cart.click()
    page.buy_checkbox.click()
    page.cookie.click()
    page.button_remove.click()

    assert page.message_remove


def test_start_registration_page(web_browser):
    """Переход на страницу оформления покупки."""
    page = CartPage(web_browser)
    page.book.click()
    page.buy_book.click()
    page.button_cart.click()
    page.button_start_registration.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/checkout/'


def test_button_deferred(web_browser):
    """Тестирование кнопки 'отложенные'."""
    page = CartPage(web_browser)
    page.button_cart.click()
    page.button_deferred.click()

    assert page.message_deferred






