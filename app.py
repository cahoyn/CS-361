import database


CONTACT_PROMPT = """
Please select from the following options:

1) Add a new contact.
2) See all contacts.
3) Find a contact by name, email, or phone.
4) Update a contact.
5) Delete a contact.
6) Exit.

Your selection: """

SEARCH_PROMPT = """Search by:

1) Name
2) Email
3) Phone

Your selection: """


def main():
    conn = database.create_connection()
    database.create_table(conn)

    while (user_input := input(CONTACT_PROMPT)) != "6":
        if user_input == "1":
            name = input("Enter contact name: ")
            email = input("Enter contact email: ")
            phone = input("Enter contact phone number: ")

            database.create_contact(conn, name, email, phone)
            print("Contact added!")
        elif user_input == "2":
            contacts = database.get_all_contacts(conn)
            for contact in contacts:
                print(f"{contact[0]} {contact[1]} {contact[2]}")
        elif user_input == "3":
            user_input = input(SEARCH_PROMPT)
            if user_input == "1":
                name = input("Enter name of contact to find: ")
                contact = database.get_contact_by_name(conn, name)
                print(f"{contact[0]}")
            if user_input == "2":
                email = input("Enter email of contact to find: ")
                contact = database.get_contact_by_email(conn, email)
                print(f"{contact[0]}")
            if user_input == "3":
                phone = input("Enter phone number of contact to find: ")
                contact = database.get_contact_by_phone(conn, phone)
                print(f"{contact[0]}")
        elif user_input == "4":
            name = input("Enter the current name of the contact you'd like to update: ")
            new_name = input("Enter the updated information. Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            database.update_contact(conn, name, new_name, email, phone)
            print("Contact updated!")
        elif user_input == "5":
            name = input("Enter the name of the contact you'd like to remove from the database: ")
            database.delete_contact(conn, name)
            print("Contact deleted.")
        else:
            print("Invalid input, please try again!")
    conn.close()


main()
