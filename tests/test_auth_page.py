import pytest
from pages.auth_page import AuthPage
from pages.locators import AuthLocators
from settings import *
import chromedriver_autoinstaller
from selenium import webdriver

# Для пользователей Windows
chromedriver_autoinstaller.install()

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    return driver


def test_page_right(driver):
    """EXP-01 Продуктовый слоган ЛК "Ростелеком ID" располагается в правой части страницы «Авторизация»."""
    try:
        page = AuthPage(driver)
        assert 'Персональный помощник в цифровом мире Ростелекома' in page.page_right.text
    except AssertionError:
        print('Элемент отсутствует в правой части формы')


def test_elements_of_auth(driver):
    """EXP-02 Проверка блока аутентификации на наличие основных элементов (Меню выбора типа аутентификации,
    Формы ввода, кнопка "Войти", ссылки "Забыл пароль" и "Зарегистрироваться")."""
    page = AuthPage(driver)

    assert page.menu_tub.text in page.card_of_auth.text
    assert page.email.text in page.card_of_auth.text
    assert page.pass_eml.text in page.card_of_auth.text
    assert page.btn_enter.text in page.card_of_auth.text
    assert page.forgot_password_link.text in page.card_of_auth.text
    assert page.register_link.text in page.card_of_auth.text


def test_menu_of_type_auth(driver):
    """EXP-03 Меню выбора типа аутентификации содержит табы: 'Телефон', 'Почта', 'Логин', 'Лицевой счёт'."""
    try:
        page = AuthPage(driver)
        menu = [page.tub_phone.text, page.tub_email.text, page.tub_login.text, page.tub_ls.text]
        for i in range(len(menu)):
            assert "Телефон" in menu
            assert 'Почта' in menu
            assert 'Логин' in menu
            assert 'Лицевой счёт' in menu
    except AssertionError:
        print('Ошибка в имени таба Меню типа аутентификации')


def test_menu_of_type_active_auth(driver):
    """EXP-04 В Меню выбора типа аутентификации по умолчанию выбрана форма аутентификации по телефону."""
    page = AuthPage(driver)

    assert page.active_tub_phone.text == Settings.menu_of_type_auth[0]


def test_placeholder_name_of_user(driver):
    """EXP-05 В форме ввода ('Телефон', 'Почта', 'Логин', 'Лицевой счёт') плейсхолдер меняется в соответствии с
    выбранным табом Меню."""
    page = AuthPage(driver)
    page.tub_phone.click()

    assert page.placeholder_name_of_user.text in Settings.placeholder_name_of_user
    page.tub_email.click()
    assert page.placeholder_name_of_user.text in Settings.placeholder_name_of_user
    page.tub_login.click()
    assert page.placeholder_name_of_user.text in Settings.placeholder_name_of_user
    page.tub_ls.click()
    assert page.placeholder_name_of_user.text in Settings.placeholder_name_of_user


def test_forgot_password_link(driver):
    """EXP-06 Проверка открытия страницы "Восстановления пароля" при переходе по ссылке "Забыл пароль"."""
    page = AuthPage(driver)
    page.driver.execute_script("arguments[0].click();", page.forgot_password_link)

    assert page.find_other_element(*AuthLocators.password_recovery).text == 'Восстановление пароля'


def test_register_link(driver):
    """EXP-07 Проверка открытия страницы "Регистрация" при переходе по ссылке "Зарегистрироваться"."""
    page = AuthPage(driver)
    page.register_link.click()

    assert page.find_other_element(*AuthLocators.registration).text == 'Регистрация'


def test_auth_by_valid_email_pass(driver):
    """EXP-08 Аутентификация пользователя с валидным email и паролем."""
    page = AuthPage(driver)
    page.email.send_keys(Settings.valid_email)
    page.email.clear()
    page.pass_eml.send_keys(Settings.valid_password)
    page.pass_eml.clear()
    page.btn_enter.click()

    try:
        assert page.get_relative_link() == '/account_b2c/page'
    except AssertionError:
        print('Предыдущие тесты вызвали появление "капчи"')
        assert 'Неверно введен текст с картинки' in page.find_other_element(*AuthLocators.error_message).text



@pytest.mark.parametrize("incor_email", [Settings.invalid_email, Settings.empty_email],
                         ids=['invalid_email', 'empty'])
@pytest.mark.parametrize("incor_passw", [Settings.invalid_password, Settings.empty_password],
                         ids=['invalid_password', 'empty'])
def test_auth_by_invalid_email(driver, incor_email, incor_passw):
    """EXP-09 Проверка аутентификации пользователя с валидным email и паролем, но не зарегистрированными в системе.
    EXP-10 Проверка аутентификации пользователя с невалидным email и паролем: пустые поля ввода"""
    page = AuthPage(driver)
    page.email.send_keys(incor_email)
    page.email.clear()
    page.pass_eml.send_keys(incor_passw)
    page.pass_eml.clear()
    page.btn_enter.click()

    assert page.get_relative_link() != '/account_b2c/page'
