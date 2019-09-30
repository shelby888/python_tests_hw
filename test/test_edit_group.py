# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="Updated", header="Updated header", footer="updated footer"))
    app.session.logout()


def test_update_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="Updated"))
    app.session.logout()


def test_update_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(header="Updated header"))
    app.session.logout()
