from flask import Flask
from models import storage

app = Flask(__name__)

# Configuration Flask supplémentaire si nécessaire

@app.teardown_appcontext
def teardown_db(exception):
    """Fermer la session de base de données à la fin de la requête ou lors de la fermeture de l'application."""
    storage.close()


def initialize_database():
    """Créer les tables dans la base de données si elles n'existent pas déjà."""
    storage.reload()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)