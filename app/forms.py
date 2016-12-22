from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    todo = StringField('Todo', [validators.Length(min=1, max=64)])
    check = BooleanField('')#, [validators.DataRequired()])

