import unittest
from selenium import webdriver


class BaseSeleniumTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()