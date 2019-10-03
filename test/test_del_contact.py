# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(Contact(firstName='test'))
    app.contacts.delete_first_contact()
