from flask import render_template, request, current_app
from flask_login import current_user, login_required
from app.email import send_email
from app.main import bp


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
