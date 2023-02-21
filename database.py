import sqlite3

print("Contacts Database Program initializing...")
print("-" * 50)

CREATE_CONTACTS_TABLE = "CREATE TABLE if not exists contacts (name TEXT PRIMARY KEY, email TEXT, phone TEXT);"
UPDATE_CONTACT = "UPDATE contacts set name = ?, email = ?, phone = ? WHERE name = ?;"
INSERT_CONTACT = "INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?);"
DELETE_CONTACT = "DELETE FROM contacts WHERE name = ?;"
GET_ALL_CONTACTS = "SELECT * FROM contacts;"
GET_CONTACT_BY_NAME = "SELECT * FROM contacts WHERE name = ?;"
GET_CONTACT_BY_EMAIL = "SELECT * FROM contacts WHERE email = ?;"
GET_CONTACT_BY_PHONE = "SELECT * FROM contacts WHERE phone = ?;"


def create_connection():
    """Create a database connection"""
    conn = None
    try:
        conn = sqlite3.connect('contacts.db')
    except sqlite3.Error as e:
        print(e)

    return conn


def create_contact(conn, name, email, phone):
    """Create a new contact"""
    with conn:
        conn.execute(INSERT_CONTACT, (name, email, phone))


def create_table(conn):
    """Create contacts table in database"""
    with conn:
        conn.execute(CREATE_CONTACTS_TABLE)


def update_contact(conn, contact_name, new_name, email, phone):
    """Update an existing contact"""
    cur = conn.cursor()
    data = (new_name, email, phone, contact_name)
    cur.execute(UPDATE_CONTACT, data)
    conn.commit()


def delete_contact(conn, contact_name):
    """Delete a contact from the database"""
    cur = conn.cursor()
    cur.execute(DELETE_CONTACT, (contact_name,))
    conn.commit()


def get_all_contacts(conn):
    """Read all contacts in table"""
    with conn:
        return conn.execute(GET_ALL_CONTACTS).fetchall()


def get_contact_by_name(conn, name):
    """Read specific contact information"""
    with conn:
        return conn.execute(GET_CONTACT_BY_NAME, (name,)).fetchall()


def get_contact_by_email(conn, email):
    """Read specific contact information"""
    with conn:
        return conn.execute(GET_CONTACT_BY_EMAIL, (email,)).fetchall()


def get_contact_by_phone(conn, phone):
    """Read specific contact information"""
    with conn:
        return conn.execute(GET_CONTACT_BY_PHONE, (phone,)).fetchall()


