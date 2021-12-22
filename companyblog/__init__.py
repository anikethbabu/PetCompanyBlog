from os import error
from flask import Flask


app = Flask(__name__)


# Regsiter views in __init__.py
from companyblog.core.views import core
from companyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)
