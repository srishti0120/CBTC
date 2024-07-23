import sys

class ContactNumber:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = ContactNumber(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Added contact: {name}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts are there as such.")
        else:
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, contact_index, name, phone, email, address):
        if 0 < contact_index <= len(self.contacts):
            self.contacts[contact_index - 1].name = name
            self.contacts[contact_index - 1].phone = phone
            self.contacts[contact_index - 1].email = email
            self.contacts[contact_index - 1].address = address
            print("Contact updated.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, contact_index):
        if 0 < contact_index <= len(self.contacts):
            removed_contact = self.contacts.pop(contact_index - 1)
            print(f"Deleted contact: {removed_contact.name}")
        else:
            print("Invalid contact index.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View contact list")
        print("3. Search contact")
        print("4. Update contact list")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)
        elif choice == '4':
            contact_manager.view_contacts()
            try:
                contact_index = int(input("Enter the contact index to update: "))
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact_manager.update_contact(contact_index, name, phone, email, address)
            except ValueError:
                print("Please enter a valid number for the contact index.")
        elif choice == '5':
            contact_manager.view_contacts()
            try:
                contact_index = int(input("Enter the contact index to delete: "))
                contact_manager.delete_contact(contact_index)
            except ValueError:
                print("Please enter a valid number for the contact index.")
        elif choice == '6':
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

