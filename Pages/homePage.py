from TestingEsanWebsite.Locators.locator import LocatorClass

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.homepage_login_link_text = "LOGIN"

    def click_homepage_login(self):
        self.driver.find_element("link text", self.homepage_login_link_text).click()
