# FILE TO CREATE DATABASE LINKED WEB FORMS - USERS SUBSECTION #
# This file is used to define and connect the web form fields with database table.


# External extensions:
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_babel import lazy_gettext
'''
(Legend)
From:
# flask_wtf: A Flask extension that integrates the WTForms library.
# flask_wtf.file: Field type classes for form fields.
# wtforms: A library that provides flexible web form rendering.
# wtforms.validators: Validator classes for form fields.
# flask_login: A Flask extension that provides user session management.
# flask_babel: A Flask extension that provides internationalization and localization.

Import:
# FlaskForm: A class for web forms with csrf protection.
# FileField: A class for file-upload field (here to upload a user's profile picture).
# FileAllowed: A class for setting valid parameters (here to upload a user's profile picture).
# StringField: A class for the base text field.
# PasswordField: A class for password field.
# SubmitField: A class for submitting web form data.
# BooleanField: A class for boolean field (True/False) (here for checkbox).
# DataRequired: A class for verifying whether a field is filled.
# Length: A class for verifying the length of the string.
# Email: A class for verifying for the email address.
# EqualTo: A class for verifying values of two fields.
# ValidationError: A class to throw a validation error.
# current_user: A function returns the proxy of the logged user.
# lazy_gettext: A function to mark text for lazy translation (translation is delayed until needed).
'''


# Internal extensions:
from flaskblog.db_models import User
'''
(Legend)
From:
# flaskblog.db_models: The db_models.py file in the root directory.

Import:
# User: A class with defined columns for the users database table.
'''


class RegistrationForm(FlaskForm):
    '''
    Class with form definitions for a registration page.

    :param FlaskForm: Class for web forms with csrf protection.

    Legend:
    # StringField(): A class for the base text field.
    # PasswordField(): A class for password field.
    # SubmitField(): A class for submitting web form data.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # DataRequired(): A class for verifying whether a field is filled.
    # Length(min=2, max=20): A class for verifying the length of the string.
    # Email(): A class for verifying for the email address.
    # EqualTo('password'): A class for verifying values of two fields.
    '''

    username = StringField(
        lazy_gettext("Username"),
        validators=[DataRequired(), Length(min=2, max=20)]
    )

    email = StringField(
        lazy_gettext("Email"),
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        lazy_gettext("Password"),
        validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        lazy_gettext("Confirm Password"),
        validators=[DataRequired(), EqualTo('password')]
    )

    submit = SubmitField(
        lazy_gettext("Sign Up")
    )

    def validate_username(self, username):
        '''
        A method for validating a username (if not in database).

        :param username: Username (from the web form).
        :return: When found, raises a ValidationError.

        Legend:
        Querying a database:
        # User.query: Query for the User database table.
        # filter_by(): Search parameters.
        # first(): Returning the first value found (end of search).

        Raising an error:
        # ValidationError(): Incorrectly entered value.
        # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
        '''

        # Querying a database:
        user = User.query.filter_by(username=username.data).first()

        # Raising an error:
        if user:
            raise ValidationError(
                lazy_gettext("That username is taken. Please choose a different one.")
            )

    def validate_email(self, email):
        '''
        A method for validating a user email (if not in database).

        :param email: Email (from the web form).
        :return: When found, raises a ValidationError.

        Legend:
        Querying a database:
        # User.query: Query for the User database table.
        # filter_by(): Search parameters.
        # first(): Returning the first value found (end of search).

        Raising an error:
        # ValidationError(): Incorrectly entered value.
        # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
        '''

        # Querying a database:
        user = User.query.filter_by(email=email.data).first()

        # Raising an error:
        if user:
            raise ValidationError(
                lazy_gettext("That email is taken. Please choose a different one.")
            )


class LoginForm(FlaskForm):
    '''
    Class with form definitions for a login page.

    :param FlaskForm: Class for web forms with csrf protection.

    Legend:
    # StringField(): A class for the base text field.
    # PasswordField(): A class for password field.
    # BooleanField(): A class for boolean field (True/False) (here for checkbox).
    # SubmitField(): A class for submitting web form data.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # DataRequired(): A class for verifying whether a field is filled.
    # Email(): A class for verifying for the email address.
    '''

    email = StringField(
        lazy_gettext("Email"),
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        lazy_gettext("Password"),
        validators=[DataRequired()]
    )

    remember_me = BooleanField(
        lazy_gettext("Remember Me")
    )

    submit = SubmitField(
        lazy_gettext("Login")
    )


class UpdateAccountForm(FlaskForm):
    '''
    Class with form definitions for user account management page.

    :param FlaskForm: Class for web forms with csrf protection.

    Legend:
    # StringField(): A class for the base text field.
    # FileField(): A class for file-upload field (here to upload a user's profile picture).
    # SubmitField(): A class for submitting web form data.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # DataRequired(): A class for verifying whether a field is filled.
    # Length(min=2, max=20): A class for verifying the length of the string.
    # Email(): A class for verifying for the email address.
    # FileAllowed(['jpg', 'png']): A class for setting valid parameters (here to upload a user's profile picture).
    '''

    username = StringField(
        lazy_gettext("Username"),
        validators=[DataRequired(), Length(min=2, max=20)]
    )

    email = StringField(
        lazy_gettext("Email"),
        validators=[DataRequired(), Email()]
    )

    picture = FileField(
        lazy_gettext("Update Profile Picture"),
        validators=[FileAllowed(['jpg', 'png'])]
    )

    submit = SubmitField(
        lazy_gettext("Update")
    )

    def validate_username(self, username):
        '''
        A method for validating a username (if not in database).

        :param username: Username (from the web form).
        :return: When found, raises a ValidationError.

        Legend:
        Username change check:
        # username.data: Content of the username field of the page.
        # current_user.username: Username of the currently logged user.

        Querying a database:
        # User.query: Query for the User database table.
        # filter_by(): Search parameters.
        # first(): Returning the first value found (end of search).

        Raising an error:
        # ValidationError(): Incorrectly entered value.
        # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
        '''

        # Username change check:
        if username.data != current_user.username:

            # (querying a database):
            user = User.query.filter_by(username=username.data).first()

            # (raising an error):
            if user:
                raise ValidationError(
                    lazy_gettext("That username is taken. Please choose a different one.")
                )

    def validate_email(self, email):
        '''
        A method for validating a user email (if not in database).

        :param email: Email (from the web form).
        :return: When found, raises a ValidationError.

        Legend:
        Username change check:
        # username.data: Content of the username field of the page.
        # current_user.username: Username of the currently logged user.

        Querying a database:
        # User.query: Query for the User database table.
        # filter_by(): Search parameters.
        # first(): Returning the first value found (end of search).

        Raising an error:
        # ValidationError(): Incorrectly entered value.
        # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
        '''

        # User email change check:
        if email.data != current_user.email:

            # (querying a database):
            user = User.query.filter_by(email=email.data).first()

            # (raising an error):
            if user:
                raise ValidationError(
                    lazy_gettext("That email is taken. Please choose a different one.")
                )


class RequestResetForm(FlaskForm):
    '''
    Class with form definitions for a password reset request page.

    :param FlaskForm: Class for web forms with csrf protection.

    Legend:
    # StringField(): A class for the base text field.
    # SubmitField(): A class for submitting web form data.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # DataRequired(): A class for verifying whether a field is filled.
    # Email(): A class for verifying for the email address.
    '''

    email = StringField(
        lazy_gettext("Email"),
        validators=[DataRequired(), Email()]
    )

    submit = SubmitField(
        lazy_gettext("Request Password Reset")
    )

    def validate_email(self, email):
        '''
        A method for validating a user email (if not in database).

        :param email: Email (from the web form).
        :return: When found, raises a ValidationError.

        Legend:
        Querying a database:
        # User.query: Query for the User database table.
        # filter_by(): Search parameters.
        # first(): Returning the first value found (end of search).

        Raising an error:
        # ValidationError(): Incorrectly entered value.
        # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
        '''

        # Querying a database:
        user = User.query.filter_by(email=email.data).first()

        # Raising an error:
        if user is None:
            raise ValidationError(
                lazy_gettext("There is no account with that email. You must register first.")
            )


class ResetPasswordForm(FlaskForm):
    '''
    Class with form definitions for a password reset page (after password reset request).

    :param FlaskForm: Class for web forms with csrf protection.

    Legend:
    # PasswordField(): A class for password field.
    # SubmitField(): A class for submitting web form data.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # DataRequired(): A class for verifying whether a field is filled.
    # EqualTo('password'): A class for verifying values of two fields.
    '''

    password = PasswordField(
        lazy_gettext("Password"),
        validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        lazy_gettext("Confirm Password"),
        validators=[DataRequired(), EqualTo('password')]
    )

    submit = SubmitField(
        lazy_gettext("Reset Password")
    )

