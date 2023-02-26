database.py and flask_app.py

UPDATED 2/26/23

These two files generate a Contacts database using sqlite3 built into Python. Flask will need to be installed if it is not already. This can be done simply by typing "pip install flask" in the terminal.

database.py contains the bulk of the code for creating the database, creating a connection to the database ('contacts.db'), and functions for creating the contacts table within the database as well as creating, reading, updating, and deleting contacts from the database.

Running flask_app.py is how the user adds and removes contacts from the database. It will run in port 5000 and clicking the link in the terminal will take you to the webpage. If there are existing contacts in the contacts.db file they will be displayed on the homepage, along with a button to Add and a button to Remove Contacts. Clicking the Remove Contact button takes you to the url /remove_contacts where you'll be prompted to enter the name of the contact you'd like to remove from the database. After hitting submit, a message will display informing the user whether the contact was deleted successfully. The user can then click the link back to the home page where they'll instantly see that that contact is no longer listed.

Similarly, the user can add a contact by hitting the Add Contact button. This takes the user to the url /enter_new where they can enter the name, email, and phone number of the contact they'd like to add to the database. After hitting submit, a message will display informing the user whether the contact was added successfully. The user can then click the link back to the home page where they'll instantly see that the new contact has been added.

home.html is the code for the homepage. contact.html is the code for adding a new contact. result.html informs the user whether their addition/removal of a contact was successful. remove.html is the code for removing a contact by entering their name.

![2023-02-13](https://user-images.githubusercontent.com/102632741/218637767-33d6c170-b310-4dc5-9740-a8a12c7a2abd.png)
