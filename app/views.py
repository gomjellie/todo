from flask import render_template, flash, make_response, session,\
	request,url_for, redirect
from app import app
from app.forms import RegistrationForm
from app.database import db_session
from app.models import Todo

@app.route('/', methods=['GET'])
def index():
    return 'a'

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

@app.route('/active', methods=['GET'])
def active():
    pass

@app.route('/completed', methods=['GET'])
def completed():
    pass

@app.route('/show', methods=['GET'])
def show():
    ret = ''
    for instance in db_session.query(Todo).order_by(Todo.id):
        ret += 'todo: {todo} is_done: {is_done}'.format(todo=instance.todo, is_done=instance.check)
    return ret

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()

