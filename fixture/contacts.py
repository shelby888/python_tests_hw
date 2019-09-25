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

    def update_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select first
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # edit
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()