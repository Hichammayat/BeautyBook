"""This module starts the beautybook Flask web application and defines endpoints
"""
from flask import request, redirect, url_for, flash, render_template, Flask
import requests  # Assurez-vous que requests est installé

app = Flask(__name__)
app.secret_key = 'beauty_app'


@app.route('/', strict_slashes=False)
def display_homepage():
    """Handles request for homepage"""
    return render_template('homepage.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        user_data = {
            'email': request.form['email'],
            'password': request.form['password'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'phone_number': request.form['phone_number'],
            'city': request.form['city']
        }

        # URL de l'API externe où vous voulez créer un utilisateur
        api_url = "http://localhost:5001/api/v1/professionals"

        try:
            # Envoyer la requête à l'API externe
            response = requests.post(api_url, json=user_data)

            # Vérifier si la requête a réussi
            if response.status_code == 201:
                flash('User successfully registered!')
                return redirect(url_for('display_homepage'))
            else:
                # Gérer les réponses d'erreur de l'API
                flash('Failed to register user. Please try again.')
        except requests.RequestException as e:
            # Gérer les exceptions de requêtes, comme un problème de réseau
            flash(str(e))

    # Si la méthode est GET ou si la création a échoué, afficher simplement le formulaire d'inscription
    return render_template('register.html')

@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session (if applicable)"""
    storage.close()``  # Si vous n'utilisez pas SQLAlchemy, cette fonction peut rester vide ou être supprimée

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
