from selenium.webdriver.common.by import By


class LoginPage():
    dictionary = {
        "txt_username": (By.NAME, 'userName'),
        "txt_password": (By.NAME, 'password'),
        "btn_login": (By.NAME, 'login')
    }
