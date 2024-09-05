from selenium.webdriver import ActionChains


class Base:
    def __init__(self,driver):
     self.driver=driver
     self.actions=ActionChains(self.driver)

     def wait_for_visibility(self, locator, timeout):
         wait = WebDriverWait(self.driver, timeout)
         condition = visibility_of_element_located(locator)
         element = wait.until(condition)

         return element


    def search_for_an_element(self,locator):
        element=self.driver.find_element(*locator)
        return element
    def click_on_an_element(self,locator):
        element=self .search_for_an_element(locator)
        element.click()

    def double_click_on_an_element(self,locator):
        actions=ActionChains(self.driver)
        element=self.search_for_an_element(locator)
        actions.double_click(element)


    def send_text_to_element(self,locator,text):
        element=self.search_for_an_element(locator)
        element.send_keys(text)

    def right_click_on_an_element(self, locators):
        element = self.search_for_an_element(locators)
        self.actions.context_click(element).perform()

    def switch_to_another_frame(self, locators, text):
        element = self.search_for_an_element(locators)
        self.driver.switch_to.frame(element)