# automated unit test to ensure a window to Edit client appears when 'Edit' link is clicked
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
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)

        # find the ‘View All Clients’ button in home screen and click it
        elem = driver.find_element_by_xpath("/html/body/div/div/p[2]/a").click()
        time.sleep(5)
        continue_test = False

        # 'Client list' page is opened when 'View All Clients' button is clicked.
        try:
            # fetch the name of the client that is to be edited
            elem = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/span[1]")
            client_name = elem.text
            time.sleep(3)
            # verify "Edit" link exists on new screen after clicking "View All Clients" button
            # and click it to open 'Edit Client' page
            elem = driver.find_element_by_xpath("/html/body/div/div[1]/p/a[1]").click()
            time.sleep(3)
            continue_test = True
        except NoSuchElementException:
            self.fail("Edit | Delete does not appear = View All Clients button not present")
            assert False
            time.sleep(1)
        except:
            self.fail("Client List page launch NOT successful - error occurred: ")
            assert False
            time.sleep(1)
        time.sleep(2)

        # if test successful so far – Check if Edit Client screen opens
        try:
            # verify "Edit" header appears on top of the page
            elem = driver.find_element_by_xpath("/html/body/div/h1").text
            time.sleep(3)
            # verify the client name in the newly opened Edit Client screen
            elem = driver.find_element_by_id("id_name")
            edit_elem = elem.get_attribute("value")
            time.sleep(3)
            # update email id field with new email id
            elem = driver.find_element_by_id("id_email")
            elem.clear()
            elem.send_keys("editEmail10@test.com")

            time.sleep(6)

            if client_name == edit_elem:
                continue_test = True
            else:
                continue_test = False

            # click the Update button
            elem = driver.find_element_by_xpath("/html/body/div/form/button").click()
            time.sleep(6)
        except NoSuchElementException:
            self.fail("Edit header does not appear = Client name text box not present")
            assert False
            time.sleep(1)
        except:
            self.fail("Edit client page launch NOT successful - error occurred: ")
            assert False
            time.sleep(1)

        if continue_test:
            try:
                # verify the edited client name appears on new screen after updating in 'Edit client' page
                elem_edited = driver.find_element_by_xpath("/html/body/div/div/h2").text
                time.sleep(3)
                # verify 'Back to All Clients' exists on new screen
                elem_back_text = driver.find_element_by_xpath("/html/body/div/p[2]").text
                time.sleep(3)
                # verify "Edit" link exists on new screen after clicking update button in 'Edit Client' page
                elem = driver.find_element_by_xpath("/html/body/div/p[1]/a[1]").text

                if elem_edited == client_name:
                    assert True
                else:
                    assert False
            except NoSuchElementException:
                self.fail("Back to All clients page launch NOT successful")
                assert False
            time.sleep(3)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
