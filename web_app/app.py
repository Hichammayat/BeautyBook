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
    if request.method == 'POST':
        # Retrieve form data
        email = request.form['email']
        password = request.form['password']
        first_name = request.form.get('first_name')  # .get allows for optional fields
        last_name = request.form.get('last_name')
        phone_number = request.form.get('phone_number')
        user_type = request.form['user_type']

        # Check if user already exists
        if storage.get(User, email):
            flash('Email already exists.')
            return redirect(url_for('register'))

        # Create and save new user
        new_user = User(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number, user_type=user_type)
        storage.new(new_user)
        storage.save()

        flash('Registration successful!')
        return redirect(url_for('display_homepage'))  # Redirect to homepage or login page

    # Show registration form
    return render_template('register.html')

@app.teardown_appcontext
def teardown_db(self):
    """removes the current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)