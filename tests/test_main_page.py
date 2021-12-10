from pages.main_page import MainPage


def test_search_field(web_browser):
    """Тестирование поле поиска."""
    page = MainPage(web_browser)
    page.search_field.send_keys('The lord of the rings')
    page.search_button.click()

    assert page.message_search


def test_message_button(web_browser):
    """Тестирование кнопки 'Сообщение'."""
    page = MainPage(web_browser)
    page.message_button.click()
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/'


def test_button_my_maze(web_browser):
    """Тестирование кнопки 'Мой лабиринт'."""
    page = MainPage(web_browser)
    page.button_my_maze.click()
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.message_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/'


def test_deferred_button(web_browser):
    """Тестирование кнопки 'Отложено'"""
    page = MainPage(web_browser)
    page.deferred_button.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_button_cart(web_browser):
    """Тестирование кнопки 'Корзина'."""
    page = MainPage(web_browser)
    page.button_cart.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cart/'


def test_shipping_and_payment(web_browser):
    """Тестирование кнопки 'Доставка и оплата'"""
    page = MainPage(web_browser)
    page.button_shipping_and_payment.click()

    assert page.get_current_url() == 'https://www.labirint.ru/help/'


def test_region_change(web_browser):
    """Тестирование выбора региона доставки."""
    page = MainPage(web_browser)
    page.region.click()
    page.field_region.send_keys("Екатеринбург")
    page.region_click.click()

    assert page.message_region


def test_button_cert(web_browser):
    """Тестирование кнопки 'Сертификаты'."""
    page = MainPage(web_browser)
    page.button_cert.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


def test_button_ratings(web_browser):
    """Тестирование кнопки 'Рейтинги'."""
    page = MainPage(web_browser)
    page.button_ratings.click()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


def test_button_new_products(web_browser):
    """Тестирование кнопки 'Новинки'."""
    page = MainPage(web_browser)
    page.button_new_products.click()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


def test_button_discount(web_browser):
    """Тестирование кнопки 'Скидки'."""
    page = MainPage(web_browser)
    page.button_discount.click()

    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'


def test_button_contact(web_browser):
    """Тестирование кнопки 'Контакты'."""
    page = MainPage(web_browser)
    page.button_contact.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


def test_button_support(web_browser):
    """Тестирование кнопки 'Поддержка'."""
    page = MainPage(web_browser)
    page.button_support.click()

    assert page.get_current_url() == 'https://www.labirint.ru/support/'


def test_button_maps(web_browser):
    """Тестирование кнопки 'Пункты самовывоза'."""
    page = MainPage(web_browser)
    page.button_maps.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


def test_more_books_with_discounts(web_browser):
    """Тестирование кнопка 'Больше книг со скидками'."""
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.more_books_with_discounts.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/sale/'


def test_footer_social_vk(web_browser):
    """Тестирование кнопки 'Вконтакте' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.vk_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirint_ru'


def test_footer_social_vk_child(web_browser):
    """Тестирование кнопки 'Вконтакте.Дети' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.vk_child_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://vk.com/labirintdeti'


def test_footer_youtube(web_browser):
    """Тестирование кнопки 'Ютьюб' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.youtube_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


def test_footer_social_instagram(web_browser):
    """Тестирование кнопки 'Инстаграм' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.instagram_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.instagram.com/labirintru/'


def test_footer_social_instagram_child(web_browser):
    """Тестирование кнопки 'Инстаграм.Дети' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.instagram_child_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.instagram.com/labirintdeti/'


def test_footer_social_facebook(web_browser):
    """Тестирование кнопки 'Фейсбук' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.facebook_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.facebook.com/labirintru'


def test_footer_social_ok(web_browser):
    """Тестирование кнопки 'Одноклассники' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.ok_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://ok.ru/labirintru'


def test_footer_social_twitter(web_browser):
    """Тестирование кнопки 'Твиттер' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.twitter_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://twitter.com/labirint_ru'


def test_footer_social_zen(web_browser):
    """Тестирование кнопки 'Дзен' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.zen_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


def test_footer_social_telegram(web_browser):
    """Тестирование кнопки 'Телеграм' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.telegram_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://t.me/labirintru'


def test_footer_social_tiktok(web_browser):
    """Тестирование кнопки 'ТикТок' в подвале сайта."""
    page = MainPage(web_browser)
    page.scroll()
    page.tiktok_footer.click()
    web_browser.switch_to.window(web_browser.window_handles[1])

    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru?'


def test_buy_book(web_browser):
    """Добавление книги в корзину."""
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.buy.click()

    assert page.message_buy


def test_compare_book(web_browser):
    """Добавление книги к сравнению."""
    page = MainPage(web_browser)
    page.scroll_part_down()
    page.scroll_part_down()
    page.more.click()
    page.compare.click()
    page.compare.click()

    assert page.message_compare

