"""This module starts the beautybook Flask web application and defines endpoints
"""

import os
from flask import request, redirect, url_for, flash, render_template, Flask, session 
import requests  # Assurez-vous que requests est installé
from models import storage

app = Flask(__name__)
app.secret_key = 'beauty_app'


@app.route('/', strict_slashes=False)
def display_homepage():
    """Handles request for homepage and fetches professionals to display"""

    api_url = "http://localhost:5001/api/v1/professionals"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            professionals = response.json()
        else:
            professionals = []
    except requests.RequestException:
        professionals = []

    return render_template('homepage.html', professionals=professionals)

@app.route('/Editprofile', strict_slashes=False)
def display_Editprofile():
    """Handles request for profilepage"""
    return render_template('Editprofile.html')

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
            'city_id': request.form['city_id']
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
    
    else:
        # Récupérer la liste des villes à partir de l'API
        cities_url = "http://localhost:5001/api/v1/cities"
        try:
            cities_response = requests.get(cities_url)
            if cities_response.status_code == 200:
                cities = cities_response.json()  # Supposons que cela renvoie une liste de villes
            else:
                cities = []
                flash('Failed to load cities.')
        except requests.RequestException as e:
            cities = []
            flash(str(e))

    # Si la méthode est GET ou si la création a échoué, afficher simplement le formulaire d'inscription
    return render_template('register.html', cities=cities)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']  # Ce sera utilisé plus tard pour l'authentification

        # Ici, nous utiliserons requests pour appeler votre API /api/v1/professionals/exist
        try:
            response = requests.post('http://localhost:5001/api/v1/professionals/exist', json={'email': email})
            if response.status_code == 200 and response.json()['exists']:
                # L'utilisateur existe, redirigez-le vers la page de profil ou autre
                # Vous devrez implémenter la logique d'authentification ici
                professional_id = response.json().get('professional_id')
                session['professional_id'] = professional_id  # Stockage de l'ID dans la session
                return redirect(url_for('display_profile'))  # Changez 'display_homepage' par votre page de profil
            else:
                flash('Email non trouvé ou mot de passe incorrect. Veuillez réessayer ou vous enregistrer.')
        except requests.RequestException as e:
            flash(str(e))

    return render_template('login.html')

@app.route('/profile', strict_slashes=False)
def display_profile():
    """Handles request for profilepage"""
    professional_id = session.get('professional_id', None)  # Assumons que l'ID est stocké en session
    if professional_id:
        try:
            response = requests.get(f'http://localhost:5001/api/v1/professionals/{professional_id}')

            if response.status_code == 200:
                user_info = response.json()
                return render_template('profile.html', user_info=user_info)
            else:
                flash('Impossible de récupérer les informations du profil.')
                return redirect(url_for('login'))
        except requests.RequestException as e:
            flash(str(e))
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    # Effacer les données de l'utilisateur de la session
    session.clear()
    # Vous pouvez aussi utiliser session.pop('professional_id', None) si vous voulez juste enlever l'ID et non effacer toute la session

    # Rediriger l'utilisateur vers la page de connexion ou la page d'accueil
    return redirect(url_for('display_homepage'))

@app.route('/AboutUs', strict_slashes=False)
def display_AboutUs():
    """Handles request for profilepage"""
    return render_template('AboutUs.html')

@app.route('/profileBook/<professional_id>', strict_slashes=False)
def display_profilebook(professional_id):
    """Handles request for profile page and fetches professional details via API."""
    api_url = f"http://localhost:5001/api/v1/professionals/{professional_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        user_info = response.json()
        return render_template('profileBooking.html', user_info=user_info)
    else:
        flash('Impossible de récupérer les informations du profil.')

@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy Session (if applicable)"""
    storage.close()  # Si vous n'utilisez pas SQLAlchemy, cette fonction peut rester vide ou être supprimée

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

