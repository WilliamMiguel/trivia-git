from flask import Blueprint, render_template, redirect, url_for, request, flash
# from app.models.mongodb.mongodb_user import User
from app.models.mongodb.mongodbquestion import Question
from app.models.modeluser import ModelUser
# from app.models.entities.user import User
# from app.utils.db import db
from app.utils.forms import FormUserLogin, FormUserRegister, FormInsertQuestion
from flask_login import current_user, LoginManager, login_user, login_required, logout_user
from app.utils.db import db
from flask_wtf.csrf import CSRFProtect

#MySQL
from app.models.mysql.user import User
from app.models.mysql.score import Score

trivia = Blueprint('trivia',__name__)
login_manager = LoginManager()
csrf = CSRFProtect()

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@trivia.route('/')
def home():
    return render_template('home.html')

@trivia.route('/index')
def index():
    return render_template("index.html")


@trivia.route('/register', methods = ["GET", "POST"])
def register():
    form = FormUserRegister()

    if form.validate_on_submit():
        if User.query.filter_by(username = form.username.data).first():
            flash("Nombre de usuario existente. Intente con otro")

        elif User.query.filter_by(email = form.email.data).first():
            flash("Email ya registrado. Intente con otro")

        else:
            user = User()
            user.name = form.name.data
            user.lastname = form.lastname.data
            user.username = form.username.data
            user.email = form.email.data
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()

            flash("Usuario registrado")

            login_user(user, remember=True)

            return redirect(url_for('trivia.register'))


    # if request.method == "POST":
    #     if form.validate_on_submit():
    #         user = User(
    #             form.name.data,
    #             form.lastname.data,
    #             form.username.data,
    #             form.email.data,
    #             form.password.data,
    #             )
    #         db.users.insert_one(user.to_json())
    #         flash("Usuario registrado", "success")

    return render_template('./auth/register.html', form = form)

@trivia.route('/login', methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("trivia.questions"))

    form = FormUserLogin()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None:
            flash("Usuario no válido")
            
        elif not user.check_password(form.password.data):
            flash("Contraseña incorrecta")

        login_user(user, remember=form.remember_me.data)

        return redirect(url_for('trivia.index'))
    
    return render_template("./auth/login.html", form = form)


    # if request.method == "POST":
    #     user = User(0, request.form["username"], request.form["password"])
    #     logged_user = ModelUser.login(db, user)
    #     if logged_user != None:
    #         if logged_user.password:
    #             login_user(logged_user)
    #             return redirect(url_for("trivia.index"))
    #         else:
    #            flash("Contraseña incorrecta")
    #            return render_template('./auth/login.html', form = form)
    #     else:
    #         flash("Usuario no encontrado")
    #         return render_template('./auth/login.html', form = form)
    #     # if form.validate_on_submit():
    #     #     pass
    # return render_template('./auth/login.html', form = form)

@trivia.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('trivia.login'))


@trivia.route('/admin/users')
def show_users():
    users = db.users.find()
    noneuser = db.users.find_one()
    return render_template('users.html', users = users, noneuser = noneuser)


@trivia.route('/questions', methods = ["GET", "POST"])
@login_required
def questions():
    # questions = db.questions.aggregate([{"$sample": {"size": 5}}])
    # nonequestion = db.questions.find_one()
    # return render_template('questions.html', questions = questions, nonequestion = nonequestion)
    return "<h1>Hola usuario</h1>"

@trivia.route('/admin/questions/insert', methods =["GET", "POST"])
def createQuestion():
    form = FormInsertQuestion()
    if request.method == "POST":
        if form.validate_on_submit():
            question = Question(
                form.question.data,
                form.option1.data,
                form.option2.data,
                form.option3.data,
                form.option4.data,
                form.answer.data
                )
            db.questions.insert_one(question.to_json())
            flash("Pregunta guardada", "success")

    return render_template('insertQuestion.html', form = form)


def status_404(error = None):
    return render_template('E404.html'), 404

def status_401(error = None):
    return render_template("./auth/unauth.html")