# Import flask
from flask import Flask

# Import a module / component
from app.mod_auth.controllers import mod_auth as auth_module

app = Flask(__name__)

# Registering components
app.register_blueprint(auth_module)
