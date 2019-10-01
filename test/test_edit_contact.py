# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstName='test'))
    app.contacts.create_contact(Contact(firstName="Update", lastName="Updator", homePhone="87654321"))
