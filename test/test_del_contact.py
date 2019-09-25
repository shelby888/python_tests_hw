def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.delete_first_contact()
    app.session.logout()