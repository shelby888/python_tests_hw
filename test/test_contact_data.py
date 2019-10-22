from random import randrange
import re


def test_contact_data_on_home_page(app):
    app.contacts.is_contact_empty_create_contact()
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstName == contact_from_edit_page.firstName
    assert contact_from_home_page.lastName == contact_from_edit_page.lastName
    assert contact_from_home_page.all_emails_from_hp == merge_emails_like_hp(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_hp == merge_phones_like_hp(contact_from_edit_page)


def test_contact_data_on_contact_view_page(app):
    app.contacts.is_contact_empty_create_contact()
    contacts_list = app.contacts.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_view_page = app.contacts.get_full_text_from_view_page(index)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.find(merge_emails_like_hp(contact_from_edit_page)) != -1
    assert contact_from_view_page.find(contact_from_edit_page.address) != -1
    assert contact_from_view_page.find(merge_full_name_like_vp(contact_from_edit_page)) != -1
    assert contact_from_view_page.find(merge_phones_like_vp(contact_from_edit_page)) != -1
    if not_empty(contact_from_edit_page.secondaryPhone):
        assert contact_from_view_page.find("P: " + contact_from_edit_page.secondaryPhone) != -1


def merge_emails_like_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))


def merge_full_name_like_vp(contact):
    return " ".join(filter(lambda x: x != "",
                           filter(lambda x: x is not None,
                                  [contact.firstName, contact.middleName, contact.lastName])))


def not_empty(s):
    return (s is not None) and (s != "")


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_hp(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homePhone, contact.mobilePhone, contact.workPhone,
                                        contact.secondaryPhone]))))


def merge_phones_like_vp(contact):
    return "\n".join(filter(lambda x: x[3:] != "",
                            ["H: " + contact.homePhone, "M: " + contact.mobilePhone, "W: " + contact.workPhone]))
