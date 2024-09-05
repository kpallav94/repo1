import allure
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver

from demowebshop.POM.homepage import HomePage
#
# @pytest.fixture()
# def driver():
#     driver=WebDriver()
#     driver.get('https://demowebshop.tricentis.com/')
#     yield driver
#     driver.quit()
@pytest.mark.skip
def test_check_for_login(driver):
    home_page_obj=HomePage(driver)
    home_page_obj.click_on_login()
    condition=driver.find_an_element("id","Email").is_displayed()
    allure.attach(driver.get_screenshot_as_png(),name="login_screenshot",attachment_type=AttachmentType.PNG)

@pytest.mark.skip
def test_check_for_register(driver):
    home_page_obj=HomePage(driver)
    home_page_obj.click_on_register()
