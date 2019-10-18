import re
from random import randrange

def test_emails_on_home_page(app):
    app.contacts.is_contact_empty_create_contact()
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_hp == merge_emails_like_hp(contact_from_edit_page)

def test_emails_on_contact_view_page(app):
    app.contacts.is_contact_empty_create_contact()
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_view_page = app.contacts.get_full_text_from_view_page(index)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.find(merge_emails_like_hp(contact_from_edit_page)) != -1

def test_address_on_home_page(app):
    app.contacts.is_contact_empty_create_contact()
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address

def test_address_on_contact_view_page(app):
    app.contacts.is_contact_empty_create_contact()
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_view_page = app.contacts.get_full_text_from_view_page(index)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.find(contact_from_edit_page.address) != -1

def merge_emails_like_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))