# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.create_contact(Contact(firstName="test 1", lastName="adasdasdsd", homePhone="12345678"))
    app.contacts.return_to_contacts_page()
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.create_contact(Contact(firstName="", lastName="", homePhone=""))
    app.contacts.return_to_contacts_page()
    app.session.logout()
