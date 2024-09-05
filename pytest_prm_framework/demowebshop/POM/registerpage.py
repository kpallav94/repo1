from demowebshop.POM.homepage import HomePage
from utilities.locators import RegisterPageLocators
class Register(HomePage):


    def register_in_application(self,fN,lN,email,pwd,cnfrmpwd):
        self.click_on_an_element(RegisterPageLocators.gender_locator)
        self.send_text_to_element(RegisterPageLocators.firstname_locator,fN)
        self.send_text_to_element(RegisterPageLocators.lastname_locator,lN)
        self.send_text_to_element(RegisterPageLocators.email_locator,email)
        self.send_text_to_element(RegisterPageLocators.password_locator,pwd)
        self.send_text_to_element(RegisterPageLocators.confirm_password_locator,cnfrmpwd)
        self.click_on_an_element(RegisterPageLocators.register_btn)

    def register_in_application_without_gender(self,fN,lN,email,pwd,cnfrmpwd):
        self.send_text_to_element(RegisterPageLocators.firstname_locator,fN)
        self.send_text_to_element(RegisterPageLocators.lastname_locator,lN)
        self.send_text_to_element(RegisterPageLocators.email_locator,email)
        self.send_text_to_element(RegisterPageLocators.password_locator,pwd)
        self.send_text_to_element(RegisterPageLocators.confirm_password_locator,cnfrmpwd)
        self.click_on_an_element(RegisterPageLocators.register_btn)
