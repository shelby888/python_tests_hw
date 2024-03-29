# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


# тест будет изменен когда добавится параметризация
# def test_update_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.update_first_group(Group(name="Updated", header="Updated header", footer="updated footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_update_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Updated")
    group.id = old_groups[index].id
    app.group.update_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# тест будет изменен когда добавится параметризация
# def test_update_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test'))
#     old_groups = app.group.get_group_list()
#     app.group.update_first_group(Group(header="Updated header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
