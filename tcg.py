from pydoc import render_doc
from flask import Flask, g, render_template,request,redirect, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

DATABASE = 'Yu gi oh.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._databse = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def home():
    cursor = get_db().cursor()
    sql = "SELECT * FROM tier"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("Arc.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('Arc.html'))
    return render_template('Arc.html', error=error)