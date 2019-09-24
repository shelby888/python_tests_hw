# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    # tests
def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstName="test 1", lastName="adasdasdsd", homePhone="12345678"))
    app.return_to_contacts_page()
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.open_add_contact_page()
    app.create_contact(Contact(firstName="", lastName="", homePhone=""))
    app.return_to_contacts_page()
    app.logout()
