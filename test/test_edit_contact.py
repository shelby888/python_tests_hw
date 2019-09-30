# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contacts.create_contact(Contact(firstName="Update", lastName="Updator", homePhone="87654321"))
