from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.user import User
from app.utils.db import db
import requests

login = Blueprint('login',__name__)