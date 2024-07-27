import locale
import os

from flask import Flask, Blueprint, session
from flask_ckeditor import CKEditor

from flask_restful import Api

from app.AppProcess import GameProcess
from app.jvt import Jwt
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user

# import flaskfilemanager

application = Flask(__name__)
application.config.from_object(Config)

db = SQLAlchemy()
db.init_app(application)
migrate = Migrate(application, db, render_as_batch=True)
jwt_tools = Jwt(Config)
login_api_routes = Blueprint('login_api', __name__, template_folder='templates')
game_api_routes = Blueprint('game_api', __name__, template_folder='templates')

# login = LoginManager(application)
# login.login_view = 'login'

# morph = pymorphy3.MorphAnalyzer()
# locale.setlocale(
#     category=locale.LC_ALL,
#     locale="Russian"
# )
locale.setlocale(locale.LC_ALL, '')

# def my_access_control_function():
#     return current_user.is_authenticated


# flaskfilemanager.init(application,
#                       custom_config_json_path="static/json/filemanager.config.json",
#                       access_control_function=my_access_control_function)

from app import routes, models
game_process = GameProcess(db, models)
from app.blueprints.api import login_api, game_api
application.register_blueprint(game_api_routes)
application.register_blueprint(login_api_routes)