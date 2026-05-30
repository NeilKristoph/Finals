contacts = []

running = True

while running:
    print("\n===== MY PHONE BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- ADD CONTACT ---")

        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = [name, phone, email, address]
        contacts.append(contact)

        print("Contact added successfully!")

    elif choice == "2":
        print("\n--- CONTACT LIST ---")

        if len(contacts) == 0:
            print("No contacts found.")

        else:
            for contact in contacts:
                print("\nName:", contact[0])
                print("Phone:", contact[1])
                print("Email:", contact[2])
                print("Address:", contact[3])

    elif choice == "3":
        print("\n--- SEARCH CONTACT ---")

        search_name = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if contact[0].lower() == search_name.lower():
                print("\nContact Found!")
                print("Name:", contact[0])
                print("Phone:", contact[1])
                print("Email:", contact[2])
                print("Address:", contact[3])

                found = True

        if found == False:
            print("Contact not found.")

    elif choice == "4":
        print("\n--- DELETE CONTACT ---")

        delete_name = input("Enter name to delete: ")

        found = False

        for contact in contacts:
            if contact[0].lower() == delete_name.lower():
                contacts.remove(contact)

                print("Contact deleted successfully!")

                found = True

                break

        if found == False:
            print("Contact not found.")

    elif choice == "5":
        print("Exiting Phone Book...")

        running = False

    else:
        print("Invalid choice. Please try again.")
