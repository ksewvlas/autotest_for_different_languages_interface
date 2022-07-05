import time
from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_displayed(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')

    assert button.is_enabled, 'Add to basket button is not displayed'
