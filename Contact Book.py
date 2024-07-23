class Contact:
    def _init_(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def _str_(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

    def search_contact(self):
        name = input("Enter the name of the contact to search: ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
        print(f"Contact {name} not found.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.delete_contact()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.view_contacts()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if _name_ == "_main_":
    main()
