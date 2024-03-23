from flask import Blueprint, render_template, session, redirect, url_for, flash, request
import requests

profile_blueprint = Blueprint('profile', __name__, template_folder='../templates')

@profile_blueprint.route('/Editprofile', strict_slashes=False)
def display_Editprofile():
    """Handles request for profilepage"""
    return render_template('Editprofile.html')

@profile_blueprint.route('/profile', strict_slashes=False)
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
                return redirect(url_for('auth.login'))
        except requests.RequestException as e:
            flash(str(e))
            return redirect(url_for('auth.login'))
    else:
        return redirect(url_for('auth.login'))

@profile_blueprint.route('/profileBook/<professional_id>', strict_slashes=False)
def display_profilebook(professional_id):
    """Handles request for profile page and fetches professional details via API."""
    api_url = f"http://localhost:5001/api/v1/professionals/{professional_id}"
    response = requests.get(api_url)
    if response.status_code == 200:
        user_info = response.json()
        return render_template('profileBooking.html', user_info=user_info)
    else:
        flash('Impossible de récupérer les informations du profil.')

  
