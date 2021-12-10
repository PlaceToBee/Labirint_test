import os
from pages.base import WebPage
from pages.elements import WebElement


class CartPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    book = WebElement(xpath='//*[@class="card-column card-column_gutter-60 swiper-slide swiper-slide-active"]')
    buy_book = WebElement(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    button_cart = WebElement(xpath='//*[@class="b-header-b-personal-e-icon b-header-b-personal-e-icon-m-cart  '
                                   'b-header-e-sprite-background"]')
    message_buy_book = WebElement(xpath='//span[Compare(test()), "1") and '
                                        '@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')
    button_remove = WebElement(xpath='//*[@id="step1-default"]/div/div/a[4]')
    message_remove = WebElement(xpath='//span[Compare(test(), "Ваша корзина пуста. Почему?") and '
                                      '@class="b-link-popup"ey g-alttext-head"]')
    buy_checkbox = WebElement(xpath='//*[@id="basket-step1-default"]/div[2]/div[2]/div/div/div[1]/div/div[6]/label'
                                    '/span')
    cookie = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[2]/button')
    button_start_registration = WebElement(xpath='//*[@id="basket-default-begin-order"]')
    button_deferred = WebElement(xpath='//*[@id="ui-id-5"]')
    message_deferred = WebElement(xpath='//*[@id="step1-put"]/div[1]/div[1]')