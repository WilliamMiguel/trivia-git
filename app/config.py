import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "Wllm.mgl34"
    MYSQL_DB = "trivia"