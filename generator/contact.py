from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(str(err))
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix='', maxlen=10):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_num(prefix='', maxlen=10):
    symbols = string.digits + " ()-" * 2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix='', maxlen=10, domainlen=5):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(symbols) for i in range(random.randrange(domainlen))]) + "." + \
           "".join([random.choice(string.ascii_letters) for i in range(random.randrange(3))])


testdata = [Contact(firstName="", lastName="", homePhone="")] + [
    Contact(firstName=random_string("name", 10), lastName=random_string("Sur", 20), homePhone=random_num("+7", 8),
            email=random_email("", 8, 5))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
