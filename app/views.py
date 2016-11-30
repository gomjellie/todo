from flask import render_template, flash, make_response, session,\
	request,url_for, redirect
from app import app
from app.forms import RegistrationForm
from app.database import db_session
from app.models import User

@app.route('/', methods=['GET'])
def index():
    return 'a'

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
    	user = User(form.username.data, 
    	        form.email.data,
    	        form.password.data)
    	db_session.add(user)
    	db_session.commit()
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

@app.route('/show', methods=['GET'])
def show():
    ret = ''
    for instance in db_session.query(User).order_by(User.id):
        ret += 'name: {0} email: {1} password: {2}'.format(instance.name, instance.email, instance.password)
    return ret

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()

