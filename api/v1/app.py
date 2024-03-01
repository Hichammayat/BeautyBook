from flask import Flask
from api.v1.views import create_v1_blueprints

app = Flask(__name__)

# Configurations supplémentaires si nécessaire
app.config['...'] = '...'

# Initialisation et enregistrement des bleus de l'API v1
create_v1_blueprints(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
