from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    # Methods for Contacts

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
