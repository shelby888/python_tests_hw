# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.update_first_group(Group(name="Updated", header="Updated header", footer="updated footer"))


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.update_first_group(Group(name="Updated"))


def test_update_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.update_first_group(Group(header="Updated header"))
