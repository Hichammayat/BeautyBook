from flask import Blueprint, render_template
import requests

static_pages_blueprint = Blueprint('static_pages', __name__, template_folder='../templates')

@static_pages_blueprint.route('/', strict_slashes=False)
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

@static_pages_blueprint.route('/AboutUs', strict_slashes=False)
def display_AboutUs():
    """Handles request for profilepage"""
    return render_template('AboutUs.html')