from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from settings import link, email_valid, password
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
from Сlasses.try_except_exception import handle_captcha


def test_email_tabs(browser):
    """Смена таба выбора аутентификации при вводе почты в табе "Телефон"""
    browser.get(link)

    # Явное ожидание таба с текстом "Телефон"
    wait = WebDriverWait(browser, 7)
    phone_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
    phone_button.click()

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError, иначе выполнится без ошибок
    handle_captcha(browser)

    # Ввод email
    username_input.send_keys(email_valid)

    # Клик по полю "Пароль"
    password_input.click()

    # Ввод пароля в поле "Пароль"
    password_input.send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(*Selectors.LOGIN_BUTTON).click()

    # Явное ожидание сообщения с текстом ошибки
    wait = WebDriverWait(browser, 3)
    error_message = wait.until(EC.visibility_of_element_located(Selectors.FORM_ERROR_MESSAGE))

    assert error_message.text == DataForAssert.ERROR_LOGIN_AND_PASSWORD_TEXT
    print()
    print()
    print(f'Вход в кабинет не выполнен, так как на странице появился текст ошибки "{error_message.text}". '
          f'Смена таба не произошла.')
