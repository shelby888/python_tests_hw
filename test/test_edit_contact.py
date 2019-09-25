# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.create_contact(Contact(firstName="Update", lastName="Updator", homePhone="87654321"))
    app.session.logout()