from flask import render_template, flash, make_response, session,\
	request,url_for, redirect
from app import app
from app.forms import RegistrationForm
from app.database import db_session
from app.models import Todo
from app.database import init_db

@app.route('/', methods=['GET'])
def index():
    init_db()
    return "Init_db"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
    	todo_list = Todo(form.todo.data,
    	        form.check.data)
    	db_session.add(todo_list)
    	db_session.commit()
    	flash('Thanks for registering')
    	return redirect(url_for('register'))
    return render_template('register.html', form=form)

@app.route('/active', methods=['GET', 'POST'])
def active():
    form = RegistrationForm(request.form)
    todos =db_session.query(Todo).filter_by(check=False).all()
    return render_template('/show.html',todos=todos,form=form)

@app.route('/completed', methods=['GET'])
def completed():
    form = RegistrationForm(request.form)
    todos = db_session.query(Todo).filter_by(check=True).all()
    return render_template('/show.html',todos=todos,form=form)

@app.route('/show', methods=['GET'])
def show():
    form = RegistrationForm(request.form)
    todos = db_session.query(Todo).all()
    return render_template("show.html",todos = todos,form=form)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()

