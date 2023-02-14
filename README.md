database.py and app.py

These two files generate a Contacts database using sqlite3 built into Python, so no additional installations are needed.

database.py contains the bulk of the code for creating the database, creating a connection to the database ('contacts.db'),
and functions for creating the contacts table within the database as well as creating, reading, updating, and deleting
contacts from the database.

app.py is what the user will interact with and it imports database. The first thing it does is create a connection to contacts.db with 
the line conn = database.create_connection(). This function in database.py specifically connects to the file "contacts.db" with the
code conn = sqlite3.connect('contacts.db'). This connection to the contacts.db file is what allows the user to REQUEST and RECEIVE
information from the file. app.py will then create the contacts table if it does not already exist with the line database.create_table(conn).
Once the connection is established and the table is confirmed to exist (with fields for contact name, email, and phone number), the user is 
prompted to select from 6 options:
 
1) Add a new contact.
2) See all contacts.
3) Find a contact by name, email, or phone.
4) Update a contact.
5) Delete a contact.
6) Exit.

While the user's input is not 6, they can continue to add contacts, see all contacts in the database, search for a contact, 
update an existing contact, or delete a contact from the database. 

1) If they choose to add a new contact, the user will be asked to enter the name, then email, then phone number of the contact.
app.py then calls database.create_contact(). The first variable is always the sqlite connection conn (no action needed), and the
remaining variables consist of the strings entered by the user. "Contact added!" will then be displayed.

2) Option 2 will display all contacts by calling database.get_all_contacts(conn) and printing the name, email, and phone number
of each contact in contacts. The sqlite connection is passed as the user's REQUEST, and the user will immediately RECEIVE the requested
information, in this case all contacts in contacts.db.

3) Option 3 displays another prompt to search by 1) name, 2) email, or 3) phone. The user will then enter the corresponding name/
email/phone and that contact's information will be printed.

4) Option 4 prompts the user to enter the current name of the contact they'd like to update. They will be asked to enter the updated
information (name, email, phone) similar to option 1 except this overwrites existing contact information. "Contact updated!"

5) Option 5 will prompt the user to enter the name of the contact they'd like to remove from the database. "Contact deleted!"

6) Option 6 closes the connection to contacts.db

![2023-02-13](https://user-images.githubusercontent.com/102632741/218637767-33d6c170-b310-4dc5-9740-a8a12c7a2abd.png)
