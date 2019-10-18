from sys import maxsize

class Contact:

    def __init__(self, id=None, firstName=None, lastName=None, middleName=None, nickName=None, address=None,
                 homePhone=None, mobilePhone=None, workPhone=None, secondaryPhone=None, all_phones_from_hp=None,
                 email=None, email2=None, email3=None, all_emails_from_hp=None):
        self.id = id
        # Name of person
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        self.nickName = nickName
        # address
        self.address = address
        # Persons tel
        self.homePhone = homePhone
        self.mobilePhone = mobilePhone
        self.workPhone = workPhone
        self.secondaryPhone = secondaryPhone
        self.all_phones_from_hp = all_phones_from_hp
        # Persons email
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_hp = all_emails_from_hp

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstName, self.lastName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastName == other.lastName and self.firstName == other.firstName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
