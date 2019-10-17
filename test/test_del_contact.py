# -*- coding: utf-8 -*-
from time import sleep
from random import randrange

from model.contact import Contact


def test_del_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(Contact(firstName='test'))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    sleep(1)
    assert len(old_contacts) - 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
