
import pickle
import os
import atexit
import sys

class Contact:
	def __init__(self, name, telephone):
		self.name = name
		self.telephone = telephone

	def modify(self, telephone):
		self.telephone = telephone

	def get_telephone(self):
		return self.telephone

path = os.path.join(sys.path[0], "addresses.data")
contacts = {}
if os.path.exists(path):
    file = open(path, "rb")
    try:
        contacts = pickle.load(file)
    except EOFError as e:
        print(e)
    file.close()

file = open(path, "wb")

def exit_handler():
    save()
    file.close()

atexit.register(exit_handler)

def add(name, telephone):
    contacts[name] = Contact(name, telephone)

def modify(name, telephone):
	if name in contacts:
    	contacts[name].modify(telephone)
    	print("Contact:", name, "updated")
    else:
    	print("Contact does not exist")

def delete(name):
	if name in contacts:
    	del contacts[name]
    	print("Contact:", name, "deleted from book")
    else:
    	print("Contact does not exist")

def search(name):
	if name in contacts:
    	return contacts[name]
    else:
    	return False


def show_all():
    for name in contacts:
        print(name, contacts[name].get_telephone())

def save():
    print("Saving contacts")
    pickle.dump(contacts, file)
    file.flush()
    print("Contacts saved")


