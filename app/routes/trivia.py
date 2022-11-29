from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.user import User
from app.models.question import Question
from app.utils.db import db
from app.utils.forms import UserLogin, UserRegister, InsertQuestion
from flask_login import current_user, LoginManager, login_user, login_required

trivia = Blueprint('trivia',__name__)

@trivia.route('/')
def home():
    return render_template('home.html')

@trivia.route('/register', methods = ["GET", "POST"])
def register():
    form = UserRegister()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(
                form.name.data,
                form.lastname.data,
                form.username.data,
                form.email.data,
                form.password.data,
                )
            db.users.insert_one(user.to_json())
            flash("Usuario registrado", "success")

    return render_template('register.html', form = form)


@trivia.route('/login', methods = ["GET", "POST"])
def login():
    form = UserLogin()

    if request.method == "POST":
        if form.validate_on_submit():
            pass
        pass
    return render_template('login.html', form = form)

@trivia.route('/users')
def show_users():
    users = db.users.find()
    noneuser = db.users.find_one()
    return render_template('users.html', users = users, noneuser = noneuser)

@trivia.route('/questions', methods = ["GET", "POST"])
def questions():
    questions = db.questions.aggregate([{"$sample": {"size": 5}}])
    nonequestion = db.questions.find_one()
    return render_template('questions.html', questions = questions, nonequestion = nonequestion)

@trivia.route('/questions/insert', methods =["GET", "POST"])
def createQuestion():
    form = InsertQuestion()
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

@trivia.errorhandler(404)
def not_found(error = None):
    return render_template('E404.html'), 404
