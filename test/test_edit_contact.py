# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(Contact(firstName='test'))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstName="Update RND", lastName="Updator", homePhone="87654321")
    contact.id = old_contacts[index].id
    app.contacts.update_contact_by_index(index, contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
