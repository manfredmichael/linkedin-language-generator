from selenium import webdriver
import time
import page

DRIVER_PATH = '../../webdriver/chromedriver'

class LinkedinPostScrapper():
    """A sample test class to show how page object works"""

    def setup(self):
        self.driver = webdriver.Chrome(DRIVER_PATH)

    def login(self):
        login_page = page.LoginPage(self.driver)
        login_page.open()
        login_page.insert_authentication()

    def main(self):
        self.setup()
        self.login()

if __name__ == '__main__':
    LinkedinPostScrapper().main()

