import os
from flask import Flask
from web_app.blueprints.auth import auth_blueprint
from web_app.blueprints.profile import profile_blueprint
from web_app.blueprints.static_pages import static_pages_blueprint

app = Flask(__name__)
app.secret_key = 'beauty_app'

# Enregistrement des blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(profile_blueprint, url_prefix='/profile')
app.register_blueprint(static_pages_blueprint)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)