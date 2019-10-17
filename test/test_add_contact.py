# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contact(firstName="test 1", lastName="adasdasdsd", homePhone="12345678")
    app.contacts.create_contact(contact)
    app.contacts.return_to_contacts_page()
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contacts.get_contact_list()
#     contact = Contact(firstName="", lastName="", homePhone="")
#     app.contacts.create_contact(contact)
#     app.contacts.return_to_contacts_page()
#     new_contacts = app.contacts.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
