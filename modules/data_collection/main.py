from selenium import webdriver
import time
import page

DRIVER_PATH = '../../webdriver/chromedriver'

driver = webdriver.Chrome(DRIVER_PATH)
p = page.LoginPage(driver)

