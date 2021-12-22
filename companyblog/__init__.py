from flask import Flask


app = Flask(__name__)


# Regsite views in __init__.py
from companyblog.core.views import core
app.register_blueprint(core)
