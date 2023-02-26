import sqlite3
from flask import Flask, render_template, request, g
import database


CREATE_CONTACTS_TABLE = "CREATE TABLE if not exists contacts (name TEXT PRIMARY KEY, email TEXT, phone TEXT);"


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


@app.route("/enternew", methods = ["POST", "GET"])
def new_contact():
    return render_template("contact.html")


@app.route('/addcon', methods = ["POST", "GET"])
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


@app.route("/delete_con", methods=["POST", "GET", "DELETE"])
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


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug = True)
