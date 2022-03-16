import utils
import element

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    def __init__(self, driver):
        self.driver = driver
        self.open()

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
        self.password_input.submit()

class SearchPage(BasePage):
    URL = 'https://www.linkedin.com/search/results/content/?keywords=achievement&sid=w9B'

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")





