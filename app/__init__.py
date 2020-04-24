from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from config import config_options

# Creating Flask Extensions Instances
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
photos = UploadSet('photos',IMAGES)
mail = 	Mail()
simple = SimpleMDE()


def create_app(config_name):
	# initialize application
	app = Flask(__name__)

	# setting up configuration
	app.config.from_object(config_options[config_name])

	# initializing flask extensions
	bootstrap.init_app(app)
	db.init_app(app)
	mail.init_app(app)
	simple.init_app(app)
	login_manager.init_app(app)
	login_manager.session_protection = 'strong'
	login_manager.login_view = 'auth.login'
	# configure UploadSet
	configure_uploads(app,photos)

	# registering the blueprint
	from .main import main as main_blueprint
	from .auth import auth as auth_blueprint


	app.register_blueprint(main_blueprint)
	app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

	# setting config
	from .request import configure_request
	configure_request(app)
	from .email import configure_email
	configure_email(app)

	return app