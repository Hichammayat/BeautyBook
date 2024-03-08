"""This module starts the beautybook Flask web application and defines endpoints
"""
from flask import request, redirect, url_for, flash, render_template, Flask
from models.user import User
from models import storage

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display_homepage():
    """handles request for homepage"""
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.teardown_appcontext
def teardown_db(self):
    """removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)