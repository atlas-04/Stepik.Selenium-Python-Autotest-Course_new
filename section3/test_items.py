#   импортируем библиотеки
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

#   тестируем наличие и видимость кнопки
def test_basket_button_find_and_displayed(browser):
    browser.get(link)
    browser.implicitly_wait(10)  #дабы не тайм слип везде
    basket_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add_to_basket_form"]/button'))) #   кнопку нашли
    assert basket_button.is_displayed() #   проверили видимость кнопки