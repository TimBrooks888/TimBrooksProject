class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def main():
    manager = ContactManager()
    manager.add_contact("Alice", "123-456-7890", "alice@example.com")
    manager.add_contact("Bob", "098-765-4321", "bob@example.com")
    manager.display_contacts()
    manager.remove_contact("Alice")
    manager.display_contacts()

if __name__ == "__main__":
    main()
