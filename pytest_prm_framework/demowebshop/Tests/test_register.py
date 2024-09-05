# from demowebshop.POM.homepage import HomePage
# from demowebshop.POM.registerpage import Register
#
# def test_register_with_all_credentials(driver):
#     home=HomePage(driver)
#     home.click_on_register()
#     register=Register(driver)
#     register.register_in_application("mota","Bheem","chota.bheem61@gmail.com","chintapakdum","chintapakdum")
#     assert driver.find_element("xpath","//input[@value='Continue']").is_displayed()
#
# def test_register_without_firstname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_in_application("", "Bheem", "chotabheem69@gmail.com", "chintapakdum", "chintapakdum")
#     assert driver.find_element("xpath","//span[contains(@for,'FirstName')]").is_displayed()
#
# def test_register_without_lastname(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_in_application("Chota", "", "chotabheem69@gmail.com", "chintapakdum", "chintapakdum")
#     assert driver.find_element("xpath","//span[contains(@for,'LastName')]").is_displayed()
#
# def test_register_without_email(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_in_application("Chota", "Bheem", "", "chintapakdum", "chintapakdum")
#     assert driver.find_element("xpath", "//span[contains(@for,'Email')]").is_displayed()
#
# def test_register_without_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_in_application("Chota", "Bheem", "chotabheem69@gmail.com", "", "chintapakdum")
#     assert driver.find_element("xpath", "//span[contains(text(),'Password')]").is_displayed()
#
# def test_register_without_confirm_password(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_in_application("Chota", "Bheem", "chotabheem69@gmail.com", "chintapakdum", "")
#     assert driver.find_element("xpath", "//span[contains(text(),'Password is required.')]").is_displayed()
#
# def test_register_without_credentials(driver):
#     home = HomePage(driver)
#     home.click_on_register()
#     register = Register(driver)
#     register.register_in_application("", "", "", "", "")
#     assert driver.find_element("xpath", "//span[contains(@for,'FirstName')]").is_displayed()
#
#     def test_register_without_gender(driver):
#         home = HomePage(driver)
#         home.click_on_register()
#         register = Register(driver)
#         register.register_in_application_without_gender("mota", "Bheem", "chota.bheem6111@gmail.com", "chintapakdum", "chintapakdum")
#         assert driver.find_element("xpath", "//input[@value='Continue']").is_displayed()
