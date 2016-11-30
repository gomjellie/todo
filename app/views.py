from flask import render_template, flash, make_response, session,\
	request,url_for, redirect
from app import app
from forms import RegistrationFormd
from database import db_session

@app.route('/', methods=['GET'])
def index():
    return 'a'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
    	user = User(form.username.data, form.email.data,
    	        form.password.data)
    	db_session.add(user)
    	flash('Thanks for registering')
    	return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET'])
def login():
    return 'loged in'

@app.route('/active', methods=['GET'])
def active():
    pass

@app.route('/completed', methods=['GET'])
def completed():
    pass

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

