import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from demowebshop.POM.homepage import HomePage


@pytest.fixture()
def driver():
    driver=WebDriver()
    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()