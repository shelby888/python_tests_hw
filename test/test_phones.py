import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contacts.get_contact_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_frome_hp == merge_phones_like_hp(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contacts.get_contact_from_view_page(0)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
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
