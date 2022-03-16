class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

class LoginPage(BasePage):
    URL = 'https://www.linkedin.com/login/in'
