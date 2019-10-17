# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(Contact(firstName='test'))
    old_contacts = app.contacts.get_contact_list()
    contact = Contact(firstName="Update", lastName="Updator", homePhone="87654321")
    contact.id = old_contacts[0].id
    app.contacts.update_first_contact(contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
