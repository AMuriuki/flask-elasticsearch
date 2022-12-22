from flask import render_template, request, current_app, g, redirect, url_for
from flask_login import current_user, login_required
from app.email import send_email
from app.main import bp
from app.main.forms import SearchForm
from app.models import Product
from app import db


@bp.route('/')
@login_required
def index():
    return render_template('index.html', title='Home')


@bp.route('/test_email', methods=['POST', 'GET'])
@login_required
def test_email():
    if request.method == "POST":
        send_email('Flask elasticsearch test email',
                   sender=current_app.config['ADMINS'][0], recipients=[request.form['recipient']], text_body=render_template('email/test_email.txt', user=current_user), html_body=render_template('email/test_email.html', user=current_user))
    return render_template('send_email.html')


@bp.before_request
def before_request():
    if current_user.is_authenticated:
        db.session.commit()
        g.search_form = SearchForm()


@bp.route('/search')
@login_required
def search():
    if not g.search_form.validate():
        print(g.search_form.errors)
    page = request.args.get('page', 1, type=int)
    products, total = Product.search(
        g.search_form.q.data, page, current_app.config['PRODUCTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['PRODUCTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title='Search', products=products, next_url=next_url, prev_url=prev_url)
