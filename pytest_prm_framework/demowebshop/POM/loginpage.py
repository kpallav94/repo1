from demowebshop.POM.homepage import HomePage

from utilities.locators import LoginPageLocators
class LogIn(HomePage):
    def login_to_the_application(self,username,password):
        self.send_text_to_element(LoginPageLocators.email_locator,username)
        self.send_text_to_element(LoginPageLocators.password_locator,password)
        self.click_on_an_element(LoginPageLocators.login_btn)


