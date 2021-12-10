from pages.cabinet_page import CabinetPage


def test_login_cabinet_page(web_browser):
    """Тестирование авторизации в кабинете."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_my_maze.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/'


def test_button_coupons(web_browser):
    """Тестирование кнопки 'Купоны'."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_coupons.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/coupons/'


def test_button_balance(web_browser):
    """Тестирование кнопки 'Баланс'."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_balance.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/balance/'


def test_button_recommendation(web_browser):
    """Тестирование кнопки 'Рекомендации'."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_recommendation.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/recommendation/'


def test_button_putorder(web_browser):
    """Тестирование кнопки 'Отложенные товары'."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_putorder.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_button_visited(web_browser):
    """Тестирование кнопки 'История просмотра'."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_visited.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/?vybor=visited'


def test_button_compare(web_browser):
    """Тестирование кнопки 'Сравнение товаров'."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_compare.click()

    assert page.get_current_url() == 'https://www.labirint.ru/compare/'


def test_button_my_actions(web_browser):
    """Тестирование кнопки 'Рецензии и подборки'."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_my_actions.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/myactions/comments/'


def test_button_personal(web_browser):
    """Тестирование кнопки 'Мои данные и настройки'."""
    page = CabinetPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.button_personal.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/personal/'



