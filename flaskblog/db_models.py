# FILE FOR CREATING CLASSES FOR DATABASE TABLES #
# This file contains classes for setting up and managing database tables.

# External extensions:
from flask import current_app
from flask_login import UserMixin
from datetime import datetime, timedelta
import jwt
'''
(Legend)
From:
# flask: A micro web framework provides libraries to build web applications.
# flask_login: A Flask extension that provides user session management.
# datetime: A library for date and time functions.

Import:
# current_app: A function providing access to a running application.
# UserMixin: Class providing default implementations for methods that Flask-Login expects user objects to have.
# datetime: Module for date and time objects.
# timedelta: Module for duration (difference between two dates, or times).
# jwt: Library for encode and decode JSON Web Tokens.
'''

# Internal extensions:
from flaskblog import db, login_manager
'''
(Legend)
From:
# flaskblog: __init__.py file in the root directory.

Import:
# db: An instance of SQLAlchemy class (used for databases).
# login_manager: Instance of LoginManager (used for login administration).
'''


@login_manager.user_loader
def load_user(author_id):
    '''
    Flask login manager definition to find and retrieve user by ID.

    :param author_id: ID of the user from the Post database table.
    :return: User data from User database table.
    '''

    return User.query.get(int(author_id))


class User(db.Model, UserMixin):
    '''
    A class for defining columns in the user database table.

    :param db.Model: Base class for all database models.
    :param UserMixin: Class providing default implementations.

    Columns defined by this class:
    # id: Post ID (table primary key, set by SQLAlchemy).
    # username: Username (set by user).
    # email: User's email (set by user).
    # profile_picture: User's profile picture (set by user or the default picture).
    # password: User's password (set by user).
    # posts: Column to link to the posts table (foreign key, set in routes).

    Legend:
    # db.Column: Class represents a column in a database table.
    # db.Integer: Specifying contents for integers.
    # db.String(#): Specifying contents for string (# represents max length).
    # primary_key=True: Setting the primary key (row ID).
    # unique=True: Setting that the field value must be unique within the column.
    # nullable=False: Setting that the field value cannot be empty.
    # default='default.jpg': Settings of default value (here determines the profile picture).
    # db.relationship: Setting up a relationship with another table.
    # 'Post': Name of the another table.
    # backref='author': Setting the relationship to the objects of the second table.
    # lazy=True: Settings for the query: fetch all available data.
    '''

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    profile_picture = db.Column(
        db.String(20),
        nullable=False,
        default='default.jpg'
    )

    password = db.Column(
        db.String(60),
        nullable=False
    )

    posts = db.relationship(
        'Post',
        backref='author',
        lazy=True
    )


    def get_reset_token(self, expires_sec=1800):
        '''
        Method for creating a JWT time token (used for password change).

        :param expires_sec: Validity period (default 30 min.).
        :return: The created token.

        Legend:
        Token parameters:
        # 'exp': Expiration time (Current time + time set by expires_sec).
        # 'sub': Subject of the JWT token (here the user ID).

        Token encode:
        # jwt.encode: Method that generates and encode the JWT token.
        # current_app.config.get('SECRET_KEY'): Setting the path to the secret key (to encrypt the token).
        # algorithm='HS256': Setting the encryption algorithm.

        '''

        token_parameters = {
            'exp': datetime.utcnow() + timedelta(days=0, seconds=expires_sec),
            'sub': self.id
        }

        return jwt.encode(
            token_parameters,
            current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )


    @staticmethod
    def verify_reset_token(token):
        '''
        Static method for validation of JWT time token (used for password change).

        :param token: The token for validation (sent by email).
        :return: First it checks if the token is valid, if so it returns the User ID, if not it returns None.

        Legend:
        Token decode:
        # jwt.decode: Method that read and decode the JWT token.
        # current_app.config.get('SECRET_KEY'): Setting the path to the secret key (to decrypt the token).
        # algorithm='HS256': Setting the decrypt algorithm.
        # ['sub']: Subject of the JWT token (here the user ID).

        Return:
        # User.query.get(user_id): Database query to obtain user data by ID
        '''

        try:
            user_id = jwt.decode(
                token,
                current_app.config.get('SECRET_KEY'),
                algorithms='HS256'
            )['sub']

        except:
            return None

        return User.query.get(user_id)


    def __repr__(self):
        '''
        Overriding of the Python dunder methods.

        :return: A machine-readable representation of the instance.
        '''

        return f"User('{self.username}', '{self.email}', '{self.profile_picture}')"


class Post(db.Model):
    '''
    A class for defining columns in the post database table.

    :param db.Model: Base class for all database models.

    Columns defined by this class:
    # id: Post ID (table primary key, set by SQLAlchemy).
    # title: Title of the post (set by user).
    # date_posted: Date posted (current day, set by SQLAlchemy).
    # content: Content of the post (set by user).
    # author_id: Author ID = User ID in User database table (foreign key, set in routes).
    # language: Language of the post (estimated on local environment, set in routes)

    Legend:
    # db.Column: Class represents a column in a database table.
    # db.Integer: Specifying contents for integers.
    # db.String(#): Specifying contents for string (# represents max length).
    # db.DateTime: Specifying contents for date and time.
    # db.Text: Specifying contents for a longer string (with a maximum length of 30,000 characters).
    # primary_key=True: Setting the primary key (row ID).
    # nullable=False: Setting that the field value cannot be empty.
    # default=datetime.utcnow: Settings of default value (here for local post creation time).
    # db.ForeignKey('user.id'): Foreign key setting (here according to the user Id column of the User database table)

    '''

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(100),
        nullable=False
    )

    date_posted = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

    language = db.Column(
        db.Text,
        nullable=False
    )


    def __repr__(self):
        '''
        Overriding of the Python dunder methods.

        :return: A machine-readable representation of the instance.
        '''

        return f"Post('{self.title}', '{self.date_posted}')"


