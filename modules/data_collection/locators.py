from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    USERNAME_TEXT_INPUT = (By.ID, 'username')
    PASSWORD_TEXT_INPUT = (By.ID, 'password')

