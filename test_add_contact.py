# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    # tests
    def test_add_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstName="test 1", lastName="adasdasdsd", homePhone="12345678"))
        self.return_to_contacts_page()
        self.logout()

    def test_add_empty_contact(self):
        self.login(username="admin", password="secret")
        self.open_add_contact_page()
        self.create_contact(Contact(firstName="", lastName="", homePhone=""))
        self.return_to_contacts_page()
        self.logout()

    # Methods
    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_contacts_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        wd = self.wd
        # init creation
        self.open_add_contact_page()
        # fill forms
        wd.find_element_by_name("firstname").send_keys(contact.firstName)
        wd.find_element_by_name("lastname").send_keys(contact.lastName)
        wd.find_element_by_name("home").send_keys(contact.homePhone)
        # submit creaton
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(wd):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
