import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class DevNetTestCases(unittest.TestCase):

    def setUp(self):
        import os
        import platform

        dir_path = os.path.dirname(os.path.realpath(__file__))
        if platform.system() == "Windows":
            chrome_driver_path = dir_path + "\\resource\\chromedriver"
        else:
            chrome_driver_path = dir_path + "/resource/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver_path)

    def test_search_in_devnet(self):
        driver = self.driver
        driver.get("https://developer.cisco.com/site/devnet/home/index.gsp")
        self.assertIn("Cisco Devnet", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("deviot")
        elem.send_keys(Keys.RETURN)
        assert "Cisco DevNet: DevNetCreations - DevIoT" not in driver.page_source

    def test_login_failed_in_devnet(self):
        driver = self.driver
        driver.get("https://developer.cisco.com/site/devnet/home/index.gsp")
        self.assertIn("Cisco Devnet", driver.title)
        elem = driver.find_element_by_link_text("Log in")
        elem.click()
        self.assertIn("Cisco.com Login Page", driver.title)
        inputName = "testuser"
        password = "123456789"

        cecName = driver.find_element_by_id("userInput")
        cecName.send_keys(inputName)
        cecpass = driver.find_element_by_id("passwordInput")
        cecpass.send_keys(password)
        login_button = driver.find_element_by_id("login-button")
        login_button.click()
        self.assertIn("Login Page", driver.title)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
