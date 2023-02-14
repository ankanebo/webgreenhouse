from flask_wtf import Form
from wtforms import BooleanField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = TextAreaField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)
