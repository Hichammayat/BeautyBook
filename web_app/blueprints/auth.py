from flask import Blueprint, request, render_template, redirect, url_for, flash
import requests

auth_blueprint = Blueprint('auth', __name__, template_folder='../templates')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
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
                return redirect(url_for('profile.display_profile'))  # Changez 'display_homepage' par votre page de profil
            else:
                flash('Email non trouvé ou mot de passe incorrect. Veuillez réessayer ou vous enregistrer.')
        except requests.RequestException as e:
            flash(str(e))

    return render_template('login.html')

@auth_blueprint.route('/logout')
def logout():
    # Effacer les données de l'utilisateur de la session
    session.clear()
    # Vous pouvez aussi utiliser session.pop('professional_id', None) si vous voulez juste enlever l'ID et non effacer toute la session

    # Rediriger l'utilisateur vers la page de connexion ou la page d'accueil
    return redirect(url_for('static_pages.display_homepage'))

@auth_blueprint.route('/register', methods=['GET', 'POST'])
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
                return redirect(url_for('static_pages.display_homepage'))
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