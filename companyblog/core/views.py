from flask import render_template,request, Blueprint
from companyblog.models import BlogPost

# core blueprint
core = Blueprint('core', __name__)

# Returns base html page
@core.route('/')
def index():
    page = request.args.get('page',1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', blog_posts= blog_posts)

# Return the company info page
@core.route('/info')
def info():
    return render_template('info.html')