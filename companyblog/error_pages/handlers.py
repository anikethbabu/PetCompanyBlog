from os import error
from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

# Returns 404 page when 404 error happens
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404

# Returns 403 page when 403 error happens
@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html') , 403