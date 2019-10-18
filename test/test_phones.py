import re
from model.contact import Contact
from random import randrange


def test_phones_on_home_page(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(Contact(firstName='test'))
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_frome_hp == merge_phones_like_hp(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contacts.count() == 0:
        app.contacts.create_contact(Contact(firstName='test'))
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_view_page = app.contacts.get_contact_from_view_page(index)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homePhone == contact_from_edit_page.homePhone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homePhone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
