# -*- coding: utf-8 -*-
from model.group import Group
# from fixture.application import Application


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="test 1", header="adasdasdsd", footer="hdscnjs kjsd"))
    app.group.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
