from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired

class FormUserRegister(FlaskForm):
    name = StringField('Nombres', validators=[DataRequired()])
    lastname = StringField('Apellidos', validators=[DataRequired()])
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    email = EmailField("Correo electrónico", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Registrar")

class FormUserLogin(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")
    submit = SubmitField("Ingresar")

class FormInsertQuestion(FlaskForm):
    question = StringField("Pregunta", validators=[DataRequired()])
    option1 = StringField("Alternativa 1", validators=[DataRequired()])
    option2 = StringField("Alternativa 2", validators=[DataRequired()])
    option3 = StringField("Alternativa 3", validators=[DataRequired()])
    option4 = StringField("Alternativa 4", validators=[DataRequired()])
    answer = StringField("Respuesta", validators=[DataRequired()])
    submit = SubmitField("Insertar pregunta")
