# automated unit test to ensure a window to Delete client appears when 'Delete' link is clicked
# in the 'Client List' page which in turn appears by clicking "View All Clients" button from home page

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class CMS_OEC(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_oec(self):

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

        # find the ‘View All Clients’ in Home page and click it
        elem = driver.find_element_by_xpath("/html/body/div/div/p[2]/a").click()
        time.sleep(5)
        continue_test = False

        try:
            # verify "Edit | Delete" exists on List client screen after clicking "View All Clients" button
            first_client_to_delete = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/span[1]").text
            time.sleep(3)
            # find 'Delete' link and click it
            elem = driver.find_element_by_xpath("/html/body/div/div[1]/p/a[2]").click()
            time.sleep(3)
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

        # if test successful so far – Check if Delete Client screen opens
        if continue_test:
            # verify the 'Delete' header exists in the new screen
            elem = driver.find_element_by_xpath("/html/body/div/h1").text
            time.sleep(3)
            # click the 'Confirm' button in the Delete page
            elem = driver.find_element_by_xpath("/html/body/div/form/button").click()
            time.sleep(6)

            # client should get deleted and navigate back to Client list page
            try:

                # verify "Edit" exists on this screen to confirm it navigated back to Client list page
                elem = driver.find_element_by_xpath("/html/body/div/div[1]/p/a[1]").text
                time.sleep(3)
                # find the name of first client in the client list screen - if client deleted successfully,
                # first client name will be different from the deleted client name
                first_client_now = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/span[1]").text
                time.sleep(6)
                if first_client_now != first_client_to_delete:
                    assert True
                else:
                    self.fail("Delete Client NOT successful")
                    assert False
            except NoSuchElementException:
                self.fail("Return to List screen NOT successful - error occurred: ")
                assert False
            time.sleep(3)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
