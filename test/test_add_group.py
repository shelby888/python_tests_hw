# -*- coding: utf-8 -*-
from model.group import Group
# from fixture.application import Application


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="test 1", header="adasdasdsd", footer="hdscnjs kjsd"))
    app.group.return_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()
