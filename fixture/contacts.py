from model.contact import Contact
import re

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def is_contact_empty_create_contact(self):
        if self.count() == 0:
            self.create_contact(Contact(firstName='test'))

    def create_contact(self, contact):
        wd = self.app.wd
        # init creation
        self.open_add_contact_page()
        # fill forms
        self.fill_contact_form(contact)
        # submit creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contacts_cache = None

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

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        # init creation
        self.open_contact_page()
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def update_contact_by_index(self, index, contact):
        wd = self.app.wd
        # init creation
        # self.open_contact_page()
        # wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        self.open_contact_to_edit_by_index(index)
        # fill forms
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_name("update").click()
        self.return_to_contacts_page()
        self.contacts_cache = None

    def update_first_contact(self, contact):
        self.update_contact_by_index(0, contact)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select first
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_css_selector("[name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastName = cells[1].text
                firstName = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contacts_cache.append(Contact(id=id, firstName=firstName, lastName=lastName, address=address,
                                                   all_phones_from_hp=all_phones, all_emails_from_hp=all_emails))
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        # Get Names
        firstName = wd.find_element_by_name("firstname").get_attribute("value")
        lastName = wd.find_element_by_name("lastname").get_attribute("value")
        middleName = wd.find_element_by_name("middlename").get_attribute("value")
        nickName = wd.find_element_by_name("nickname").get_attribute("value")
        # get address
        address = wd.find_element_by_name("address").text
        # Get Telephone
        homePhone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        # Get emails
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstName=firstName, lastName=lastName, middleName=middleName, nickName=nickName, address=address,
                       homePhone=homePhone, mobilePhone=mobilephone, workPhone=workphone, secondaryPhone=secondaryphone,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homePhone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homePhone=homePhone, mobilePhone=mobilephone, workPhone=workphone, secondaryPhone=secondaryphone)

    def get_full_text_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        return wd.find_element_by_id("content").text

