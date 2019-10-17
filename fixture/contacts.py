from model.contact import Contact


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
        self.fill_contact_form(contact)
        # submit creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstName)
        self.change_field_value("lastname", contact.lastName)
        self.change_field_value("home", contact.homePhone)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def update_first_contact(self, contact):
        wd = self.app.wd
        # init creation
        self.open_contact_page()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # fill forms
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("[name='entry']"):
            cells = element.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_name("selected[]").get_attribute("value")
            lastName = cells[1].text
            firstName = cells[2].text
            phone = cells[5].text
            contacts.append(Contact(firstName=firstName, lastName=lastName, homePhone=phone, id=id))
        return contacts





