# -*- coding: utf-8 -*-
from time import sleep

from model.contact import Contact


def test_del_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(Contact(firstName='test'))
    old_contacts = app.contacts.get_contact_list()
    app.contacts.delete_first_contact()
    sleep(1)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
