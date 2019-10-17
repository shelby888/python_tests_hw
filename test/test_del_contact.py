# -*- coding: utf-8 -*-
from time import sleep

from model.contact import Contact


def test_del_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(Contact(firstName='test'))
    old_contacts = app.contacts.get_contact_list()
    app.contacts.delete_first_contact()
    sleep(1)
    assert len(old_contacts) - 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
