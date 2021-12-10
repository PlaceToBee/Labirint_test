from pages.login_page import LoginPage


def test_login_page_with_positive_code(web_browser):
    """Тестирование авторизации с зарегистрированным кодом."""
    page = LoginPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-92AB')
    page.auth_btn.click()
    page.close_btn.click()
    page.main_page_btn.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


def test_login_page_with_negative_code(web_browser):
    """Тестирование авторизации с неверным кодом."""
    page = LoginPage(web_browser)
    page.auth_field.send_keys('A8AF-452F-2222')
    page.auth_field.click()

    assert page.fail

def test_login_page_all_auth(web_browser):
    """Тестирование кнопки 'Другие способы ввода'."""
    page = LoginPage(web_browser)
    page.auth_all.click()

    assert page.auth_all_message
