from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class UserRegister(FlaskForm):
    name = StringField('Nombres', validators=[DataRequired()])
    lastname = StringField('Apellidos', validators=[DataRequired()])
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    email = EmailField("Correo electrónico", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Registrar")

class UserLogin(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")
    submit = SubmitField("Ingresar")
