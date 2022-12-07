from TestingEsanWebsite.Locators.locator import LocatorClass


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_name = LocatorClass.email_textbox_name
        self.password_textbox_name = LocatorClass.password_textbox_name
        self.login_button_xpath = LocatorClass.login_button_xpath

    def enter_email(self, username):
        self.driver.find_element("name", self.email_textbox_name).clear()
        self.driver.find_element("name", self.email_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("name", self.password_textbox_name).clear()
        self.driver.find_element("name", self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element("xpath", self.login_button_xpath).click()

