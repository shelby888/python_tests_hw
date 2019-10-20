import re
from random import randrange


def test_phones_on_home_page(app):
    app.contacts.is_contact_empty_create_contact()
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_frome_hp == merge_phones_like_hp(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    app.contacts.is_contact_empty_create_contact()
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_view_page = app.contacts.get_full_text_from_view_page(index)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.find(merge_phones_like_vp(contact_from_edit_page)) != -1
    # assert contact_from_view_page.homePhone == contact_from_edit_page.homePhone
    # assert contact_from_view_page.workPhone == contact_from_edit_page.workPhone
    # assert contact_from_view_page.mobilePhone == contact_from_edit_page.mobilePhone
    # assert contact_from_view_page.secondaryPhone == contact_from_edit_page.secondaryPhone
    if not_empty(contact_from_edit_page.secondaryPhone):
        assert contact_from_view_page.find("P: " + contact_from_edit_page.secondaryPhone) != -1


def not_empty(s):
    return (s is not None) and (s != "")


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homePhone, contact.mobilePhone, contact.workPhone, contact.secondaryPhone]))))

def merge_phones_like_vp(contact):
    return "\n".join(filter(lambda x: x[3:] != "",
                            ["H: " + contact.homePhone, "M: " + contact.mobilePhone, "W: " + contact.workPhone]))