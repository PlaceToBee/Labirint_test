from pages.base import WebPage
from pages.elements import WebElement


class CabinetPage(WebPage):

    def __init__(self, web_browser):
        url = 'https://www.labirint.ru/cabinet/'
        super().__init__(web_browser, url)

    auth_field = WebElement(xpath='/html/body/div[1]/div[1]/div/div/div/div/div[1]/form[1]/div[3]/input')
    auth_btn = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    close_btn = WebElement(xpath='//*[@id="auth-success-login"]/input[2]')
    button_my_maze = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]')
    button_coupons = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[3]/a[1]/span[1]')
    button_balance = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[4]/a[1]')
    button_recommendation = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[5]/a[1]')
    button_putorder = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[6]/a[1]')
    button_visited = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[7]/a[1]')
    button_compare = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[8]/a[1]')
    button_my_actions = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[9]/a[1]')
    button_personal = WebElement(xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[2]/ul[1]/li[10]/a[1]')
    ex_message = WebElement(xpath='//*[@id="auth-by-code"]/div[1]')

