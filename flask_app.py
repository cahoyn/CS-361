# Author: Nathan Cahoy
# Date: 2/26/2023
# Class: CS361
# Description: Example UI for partner's term project. Uses Flask with database.py to make changes to
# contacts.db via html. Currently capable of adding and deleting contacts.

import sqlite3
from flask import Flask, render_template, request, g
import database


app = Flask(__name__)
app.secret_key = "mdvojbnoneflkjnc"


@app.route('/')
def home():
    con = database.create_connection()
    database.create_table(con)
    cur = con.cursor()
    con.row_factory = sqlite3.Row
    cur.execute("select * from contacts")
    rows = cur.fetchall()
    return render_template('home.html', rows=rows)


@app.route("/remove_contacts", methods=["POST"])
def remove_contacts():
    return render_template("remove.html")


@app.route("/enter_new", methods=["POST", "GET"])
def new_contact():
    return render_template("contact.html")


@app.route('/addcon', methods=["POST", "GET"])
def addcon():
    con = database.create_connection()
    database.create_table(con)
    cur = con.cursor()
    if request.method == 'POST':
        try:
            name = request.form["name"]
            email = request.form['email']
            phone = request.form['phone']

            database.create_contact(con, name, email, phone)
            con.commit()
            msg = "Contact added successfully."
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template("result.html", msg=msg)


@app.route("/delete_con", methods=["POST", "GET"])
def delete_con():
    con = database.create_connection()
    if request.method == 'POST':
        try:
            name = request.form["name"]
            database.delete_contact(con, name)
            con.commit()
            msg = "Contact deleted successfully."
        except:
            con.rollback()
            msg = "Error in delete operation"
        finally:
            return render_template("result.html", msg=msg)


if __name__ == '__main__':
    app.run(debug = True)
