from flask import render_template,request, Blueprint


# core blueprint
core = Blueprint('core', __name__)

# Returns base html page
@core.route('/')
def index():
    # more code needed
    return render_template('index.html')

# Return the company info page
@core.route('/info')
def info():
    return render_template('info.html')