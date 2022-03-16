import utils
import element

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

class LoginPage(BasePage):
    URL = 'https://www.linkedin.com/login'
    username_input = element.UsernameInputElement()
    password_input = element.PasswordInputElement()

    def login(self):
        self.insert_authentication()

    def insert_authentication(self):
        username, password = utils.Authentication().get_authentication()
        self.username_input = username
        self.password_input = password
        print(self.username_input)





