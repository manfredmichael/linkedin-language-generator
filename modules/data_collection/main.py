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
        login_page.login()

    def main(self):
        self.setup()
        self.login()

    def tear_down(self):
        self.driver.close()

if __name__ == '__main__':
    scrapper = LinkedinPostScrapper()
    try:
        scrapper.main()
    finally:
        time.sleep(20)
        scrapper.tear_down()


