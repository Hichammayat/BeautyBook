import os
from flask import Flask, render_template, session, redirect, url_for, flash, request
from web_app.blueprints.auth import auth_blueprint
from web_app.blueprints.profile import profile_blueprint
from web_app.blueprints.static_pages import static_pages_blueprint
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'beauty_app'

# Enregistrement des blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(profile_blueprint, url_prefix='/profile')
app.register_blueprint(static_pages_blueprint)

mail_password = os.environ.get('MAIL_PASSWORD')


# Configuration de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'h.mayat@mundiapolis.ma'  # Votre adresse Gmail
app.config['MAIL_PASSWORD'] = mail_password

# Initialisation de Flask-Mail
mail = Mail(app)

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    client_firstname = request.form['client_firstname']
    client_lastname = request.form['client_lastname']
    client_phone = request.form['client_phone']
    appointment_time = request.form['appointment_time']
    professional_email = request.form['professional_email']  # L'email du professionnel

    subject = "New Booking Request"
    sender = app.config['MAIL_USERNAME']
    recipients = [professional_email]
    body = f"""\
    New Booking Request:
    First Name: {client_firstname}
    Last Name: {client_lastname}
    Phone: {client_phone}
    Appointment Time: {appointment_time}
    """

    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = body

    try:
        mail.send(msg)
        flash("Booking request sent successfully.")
        return redirect(url_for('static_pages.thank_you'))
    except Exception as e:
        flash(f"An error occurred: {e}")

    return redirect(url_for('profile.display_profile',))

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)