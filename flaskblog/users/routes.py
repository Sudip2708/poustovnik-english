# FILE FOR BUILDING WEB PAGES - USERS SUBSECTION #
# This file is used to define and create web pages of the application.


# External extensions:
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from flask_babel import lazy_gettext
'''
(Legend)
From:
# flask: A micro web framework provides libraries to build web applications.
# flask_login: A Flask extension that provides user session management.
# flask_babel: A Flask extension that provides internationalization and localization.

Import:
# Blueprint: A class providing structuring of the application.
# render_template: A function for rendering of an html template (based on the Jinja2 engine).
# request: A function for processing data sent from the client to the server.
# redirect: A function for redirecting users to a specific URL.
# url_for: A function for generate an URL (for a given endpoint).
# flash: A function for display an informational messages.
# current_user: A function returns the proxy of the logged user.
# login_user: A function for managing user login.
# logout_user: A function for managing user logout.
# login_required: A function to verify if the user is login.
# lazy_gettext: A function to mark text for lazy translation (translation is delayed until needed).
'''


# Internal extensions:
from flaskblog import Locale, db, bcrypt
from flaskblog.db_models import User
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from flaskblog.users.utils import save_picture, send_reset_email
'''
(Legend)
From:
# flaskblog: The __init__.py file in the root directory.
# flaskblog.db_models: The db_models.py file in the root directory.
# flaskblog.users.forms: The forms.py file in the users folder in the root directory.
# flaskblog.users.utils: The utils.py file in the users folder in the root directory.

Import:
# Locale: A class providing language settings.
# db: An instance of SQLAlchemy class (used for databases).
# bcrypt: An instance of Bcrypt class (used for encryption).
# User: A class with defined columns for the users database table.
# RegistrationForm: A class to manage the form data on the page (here for registration).
# LoginForm: A class to manage the form data on the page (here for login).
# UpdateAccountForm: A class to manage the form data on the page (here for user account management).
# RequestResetForm: A class to manage the form data on the page (here for password reset request).
# ResetPasswordForm: A class to manage the form data on the page (here for password reset, after request).
# save_picture: A functions for processing and saving a profile picture.
# send_reset_email: A function to send an email with a time token for password change.
'''


# Page blueprint settings:
users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    '''
    Route function for creating a registration page.

    :return: Registration page.

    Legend:
    Decorator:
    # @users.route("/register"): Defining the page address (by root directory).
    # methods=['GET', 'POST']: Defining the methods used for the page.

    User logging check:
    # current_user.is_authenticated: Verification of whether the user (current_user) is logged in (is_authenticated).
    # redirect(url_for('main.home')): Redirecting (redirect) to the url (url_for) for home page ('main.home').

    Entry form validation:
    # RegistrationForm(): A class to manage the form data on the page (here for registration).
    # validate_on_submit(): A shortcut for is_submitted() and validate().

    Hashing password:
    # bcrypt.generate_password_hash(): Bcrypt class method for hashing (here to hide the password).
    # form.password.data: Content of the password field from the page form.
    # decode('utf-8'): Encode settings.

    Entering data into database:
    # user: An instance of the User class for user data.
    # db.session.add(user): Adding data to the database.
    # db.session.commit(): Commit changes to the database.

    Info message:
    # flash(): A function for display an informational messages.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # 'success': Message category.

    Redirecting:
    # redirect(url_for('users.login')): Redirecting (redirect) to the url (url_for) for login page ('users.login').

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'users_register.html': Name of the html file (in the template directory).
    # title='Register': Page title.
    # form=form: Page form.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    '''

    # User logging check:
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Entry form validation:
    form = RegistrationForm()
    if form.validate_on_submit():

        # (hashing password):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # (entering data into database):
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        # (info message & redirecting):
        flash(lazy_gettext("Your account has been created! You are now able to log in"), 'success')
        return redirect(url_for('users.login'))

    # Page rendering:
    return render_template(
        'users_register.html',
        title='Register',
        form=form,
        language=Locale.current.language
    )


@users.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Route function for creating a login page.

    :return: Login page.

    Legend:
    Decorator:
    # @users.route("/login"): Defining the page address (by root directory).
    # methods=['GET', 'POST']: Defining the methods used for the page.

    User logging check:
    # current_user.is_authenticated: Verification of whether the user (current_user) is logged in (is_authenticated).
    # redirect(url_for('main.home')): Redirecting (redirect) to the url (url_for) for home page ('main.home').

    # Entry form validation:
    # LoginForm(): A class to manage the form data on the page (here for login).
    # validate_on_submit(): A shortcut for is_submitted() and validate().

    Email validation:
    # User.query: Query for the User database table.
    # filter_by(): Search parameters.
    # first(): Returning the first value found (end of search).

    Login:
    # bcrypt.check_password_hash(): A method of the Bcrypt class to decode the hash (here to verify the password).
    # user.password: Content from the user database table.
    # form.password.data: Content of the password field from the page form.

    Redirecting:
    # request.args.get('next'): A method to access the URL parameter value.
    # redirect(next_page): Redirecting (redirect) to the next page (next_page).
    # redirect(url_for('main.home')): Redirecting (redirect) to the url (url_for) for home page ('main.home').

    Error message:
    # flash(): A function for display an informational messages.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # 'danger': Message category.

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'users_login.html': Name of the html file (in the template directory).
    # title='Login': Page title.
    # form=form: Page form.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    '''

    # User logging check:
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Entry form validation:
    form = LoginForm()
    if form.validate_on_submit():

        # (email validation):
        user = User.query.filter_by(email=form.email.data).first()

        # (login & redirecting):
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))

        # (error message):
        else:
            flash(lazy_gettext("Login Unsuccessful. Please check email and password"),'danger')

    # Page rendering:
    return render_template(
        'users_login.html',
        title='Login',
        form=form,
        language=Locale.current.language
    )


@users.route("/logout")
def logout():
    '''
    Route function for creating a logout page.

    :return: Logout page.

    Legend:
    Decorator:
    # @users.route("/logout"): Defining the page address (by root directory).

    Logout:
    # logout_user(): A function for managing user logout.

    Redirecting:
    # redirect(url_for('main.home')): Redirecting (redirect) to the url (url_for) for home page ('main.home').
    '''

    # Logout & Redirecting:
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    '''
    Route function for creating a user account management page.

    :return: User account management page.

    Legend:
    Decorator:
    # @users.route("/account"): Defining the page address (by root directory).
    # methods=['GET', 'POST']: Defining the methods used for the page.
    # @login_required: Permission for logged users only.

    Entry form validation:
    # UpdateAccountForm(): A class to manage the form data on the page (here for user account management).
    # validate_on_submit(): A shortcut for is_submitted() and validate().

    Entering data into database:
    # form.picture.data: Image from page form.
    # save_picture(): A functions for processing and saving a profile picture.
    # current_user: A function returns the proxy of the logged user.
    # form.xxx.data: Page form data.
    # db.session.commit(): Commit changes to the database.

    Info message:
    # flash(): A function for display an informational messages.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # 'success': Message category.

    Redirecting:
    # redirect(url_for('users.account')): Redirecting (redirect) to the url (url_for) for account page ('users.account').

    Data pre-filling:
    # request.method == 'GET': A condition to check for data retrieved.
    # current_user: A function returns the proxy of the logged user.
    # form.xxx.data: Page form data.

    Profile picture URL:
    # 'static': The name of the main folder.
    # filename='profile_pictures/': The name of the subfolder.
    # current_user.profile_picture: The name of the file.

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'users_account.html': Name of the html file (in the template directory).
    # title='Account': Page title.
    # profile_picture=profile_picture: Profile picture.
    # form=form: Page form.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    '''

    # Entry form validation:
    form = UpdateAccountForm()
    if form.validate_on_submit():

        # (entering data into database):
        if form.picture.data:
            current_user.profile_picture = save_picture(form.picture.data)
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()

        # (info message & redirecting):
        flash(lazy_gettext("Your account has been updated!"), 'success')
        return redirect(url_for('users.account'))

    # Data pre-filling:
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    # Profile picture URL:
    profile_picture = url_for('static', filename='profile_pictures/' + current_user.profile_picture)

    # Page rendering:
    return render_template(
        'users_account.html',
        title='Account',
        profile_picture=profile_picture,
        form=form,
        language=Locale.current.language
    )


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    '''
    Route function for creating a password change request page.

    :return: Password change request page.

    Legend:
    Decorator:
    # @users.route("/reset_password"): Defining the page address (by root directory).
    # methods=['GET', 'POST']: Defining the methods used for the page.

    User logging check:
    # current_user.is_authenticated: Verification of whether the user (current_user) is logged in (is_authenticated).
    # redirect(url_for('main.home')): Redirecting (redirect) to the url (url_for) for home page ('main.home').

    # Entry form validation:
    # RequestResetForm(): A class to manage the form data on the page (here for password reset request).
    # validate_on_submit(): A shortcut for is_submitted() and validate().

    User verification and email sending:
    # User.query: Query for the User database table.
    # filter_by(): Search parameters.
    # first(): Returning the first value found (end of search).
    # send_reset_email(user): A function to send an email with a time token for password change.

    Info message:
    # flash(): A function for display an informational messages.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # 'success': Message category.

    Redirecting:
    # redirect(url_for('users.account')): Redirecting (redirect) to the url (url_for) for account page ('users.account').

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'users_reset_request.html': Name of the html file (in the template directory).
    # title='Reset Password': Page title.
    # form=form: Page form.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    '''

    # User logging check:
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Entry form validation:
    form = RequestResetForm()
    if form.validate_on_submit():

        # (user verification and email sending):
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)

        # (info message & redirecting):
        flash(lazy_gettext("An email has been sent with instructions to reset your password."), 'info')
        return redirect(url_for('users.login'))

    # Page rendering:
    return render_template(
        'users_reset_request.html',
        title='Reset Password',
        form=form,
        language=Locale.current.language
    )


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    '''
    Route function for creating a password change page.

    :param username: Email token (from page address).
    :return: Password change page.

    Legend:
    Decorator:
    # @users.route("/reset_password/<token>"): Defining the page address (by root directory).
    # methods=['GET', 'POST']: Defining the methods used for the page.

    User logging check:
    # current_user.is_authenticated: Verification of whether the user (current_user) is logged in (is_authenticated).
    # redirect(url_for('main.home')): Redirecting (redirect) to the url (url_for) for home page ('main.home').

    Token validation:
    # User.verify_reset_token(token): A User method to validate the token.

    Info message:
    # flash(): A function for display an informational messages.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # 'success': Message category.

    Redirecting:
    # url_for():  A function for generate an URL (for a given endpoint).

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'users_reset_token.html': Name of the html file (in the template directory).
    # title='Reset Password': Page title.
    # form=form: Page form.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    '''

    # User logging check:
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    # Token validation:
    user = User.verify_reset_token(token)
    if user is None:

        # (info message & redirecting):
        flash(lazy_gettext("That is an invalid or expired token"), 'warning')
        return redirect(url_for('users.reset_request'))

    # Entry form validation:
    form = ResetPasswordForm()
    if form.validate_on_submit():

        # (hashing password):
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # (entering data into database):
        user.password = hashed_password
        db.session.commit()

        # (info message & redirecting):
        flash(lazy_gettext("Your password has been updated! You are now able to log in"), 'success')
        return redirect(url_for('users.login'))

    # Page rendering:
    return render_template(
        'users_reset_token.html',
        title='Reset Password',
        form=form,
        language=Locale.current.language
    )

