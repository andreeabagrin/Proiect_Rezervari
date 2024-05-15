from flask import Flask, url_for
from config import Config
from app.Creational import DatabaseSession
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = DatabaseSession(app)
migrate = Migrate(app, db)
login=LoginManager(app)
login.login_view='login' # specify the login page to redirect when require login

from app import routes,models,Creational