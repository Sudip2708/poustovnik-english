# APPLICATION INITIALIZATION FILE #
# This file is used for creation and basic configuration of the application.


# External extensions:
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_babel import Babel
from babel import Locale
'''
(Legend)
From:
# flask: A micro web framework provides libraries to build web applications.
# flask_login: A Flask extension that provides user session management.
# flask_sqlalchemy: A Flask extension that provides tools and methods for interacting with the database.
# flask_bcrypt: A Flask extension that provides bcrypt hashing.
# flask_mail: A Flask extension that provides email management and sending.
# flask_babel: A Flask extension that provides internationalization and localization.
# babel: A library that provides internationalization and localization.

Import:
# Flask: A class providing creating web applications.
# LoginManager: A class providing user session management.
# SQLAlchemy: A class providing database management.
# Bcrypt: A class providing bcrypt hashing.
# Mail: A class providing mail management.
# Babel: A class providing internationalization and localization.
# Locale: A class providing language settings.
'''


# Internal extensions:
from flaskblog.config import Config
'''
(Legend)
From:
# flaskblog.config: The config.py file in the root directory.

Import:
# Config: A class with the basic configuration for the application.
'''


# Modules initialization:
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
mail = Mail()
'''
(Legend)
# db: An instance of SQLAlchemy class (used for databases).
# bcrypt: An instance of Bcrypt class (used for encryption).
# login_manager: An instance of LoginManager class (used for login administration).
# login_manager.login_view: Setting the login access page.
# login_manager.login_message_category: Settings for login notification.
# mail: An instance of Mail class (used for sending emails).
'''


# Locale settings:
us = Locale('en', 'US')
cz = Locale('cs', 'CZ')
Locale.current = cz
Locale.post_to_translate = [None,]
'''
(Legend)
# us: An instance of Locale class (settings for Englich).
# cz: An instance of Locale class (settings for Czech).
# Locale.current: A class attribute for selected language.
# Locale.post_to_translate: A class attribute for translations from Google translator.
'''


def get_locale():
    '''
    Function for setting the language of the page.

    :return: Page in selected language.

    Legend:
    # Locale.current: Class attribute for selected language.
    '''

    return Locale.current


def create_app(config_class=Config):
    '''
    Functions for creating and configuration of the application.

    :param config_class: Reference to the configuration class.
    :return: Created application.

    Legend:
    # app: A flask instance for the application.
    # Flask(__name__): Flask class with root settings.
    # config.from_object(Config): Definition of the path to the configuration file.
    # init_app(app): Assign modules to the application.
    # from flaskblog._._: Application file path.
    # import _: A name of the blueprints.
    # register_blueprint(_): Method for registering blueprints.
    # Babel: Class provides an interface for page localization.
    # locale_selector=get_locale: Binding the page language to the get_locale function.
    '''

    # Setting app as a Flask instance:
    app = Flask(__name__)

    # Load the configurations:
    app.config.from_object(Config)

    # Assignment of instances:
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Import blueprints:
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    # Registration of blueprints:
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    # Instance of Babel (for web localization):
    babel = Babel(app, locale_selector=get_locale)

    return app

