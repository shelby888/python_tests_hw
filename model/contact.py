from sys import maxsize

class Contact:

    def __init__(self, id=None, firstName=None, lastName=None,
                 homePhone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_frome_hp=None):
        self.firstName = firstName
        self.lastName = lastName
        self.homePhone = homePhone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_frome_hp=all_phones_frome_hp


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstName, self.lastName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastName == other.lastName and self.firstName == other.firstName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


