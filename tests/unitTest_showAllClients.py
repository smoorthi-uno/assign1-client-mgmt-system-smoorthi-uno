# automated unit test to ensure a window to show list of clients appears
# when the "View All Clients" button is clicked

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_SAC(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cms(self):

        # login from the admin pane
        user = "smoorthi"
        pwd = "swethacse"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)

        # find the ‘View All Clients’ in the home screen and click it
        elem = driver.find_element_by_xpath("/html/body/div/div/p[2]/a").click()
        time.sleep(5)
        continue_test = True

        # if test successful so far – Check if Client list screen opens
        if continue_test:
            try:
                # verify the name of the client exits on new screen after clicking "View All Clients" button
                elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/span[1]")
                client_name = elem.text
                time.sleep(3)
                # verify "Edit" exists on new screen after clicking "View All Clients" button
                elem = driver.find_element_by_xpath("/html/body/div/div[1]/p/a[1]").text
                time.sleep(3)
                # verify "Delete" exists on new screen after clicking "View All Clients" button
                elem = driver.find_element_by_xpath("/html/body/div/div[1]/p/a[2]").text

                continue_test = True
            except NoSuchElementException:
                self.fail("Edit | Delete does not appear = View All Clients button not present")
                assert False
                time.sleep(1)
            except:
                self.fail("List post NOT successful - error occurred: ")
                assert False
                time.sleep(1)
            time.sleep(2)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
