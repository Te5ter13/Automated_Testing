import HtmlTestRunner
from selenium import webdriver
import time
import unittest

#running from terminal
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from TestingEsanWebsite.Pages.loginPage import LoginPage
from TestingEsanWebsite.Pages.homePage import HomePage

class TestingESAN(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(
            executable_path='/usr/local/bin/geckodriver'
        )
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        try:
            self.driver.get("YOUR_BASE_URI")
        except Exception as e:
            print(e)
        else:
            self.driver.implicitly_wait(5)

    def test_login_valid(self):
        driver = self.driver
        login_click = HomePage(driver)
        login_click.click_homepage_login()

        login = LoginPage(driver)
        time.sleep(5)
        login.enter_email("YOUR_USERNAME")
        login.enter_password("YOUR_PASSWORD")
        time.sleep(5)
        login.click_login()

    @classmethod
    def tearDownClass(self):
        time.sleep(5)
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='TestingEsanWebsite/Reports'))

