class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact):
        wd = self.app.wd
        # init creation
        self.open_add_contact_page()
        # fill forms
        wd.find_element_by_name("firstname").send_keys(contact.firstName)
        wd.find_element_by_name("lastname").send_keys(contact.lastName)
        wd.find_element_by_name("home").send_keys(contact.homePhone)
        # submit creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def update_first_contact(self, contact):
        wd = self.app.wd
        # init creation
        self.open_contact_page()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # fill forms
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstName)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastName)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homePhone)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()