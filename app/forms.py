from wtforms import Form, BooleanField, StringField, PasswordField, validators

#class RegistrationForm(Form):
#    username = StringField('Username', [validators.Length(min=4, max=64)])
#    email = StringField('Email Address', [validators.Length(min=6, max=64)])
#    password = PasswordField('New Password', [
#        validators.DataRequired(),
#        validators.EqualTo('confirm', message='Passwords must match')])
#    confirm = PasswordField('Repeat Password')
#    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
#

class RegistrationForm(Form):
    todo = StringField('Todo', [validators.Length(min=1, max=64)])
    check = BooleanField('I\'ve done this', [validators.DataRequired()])

