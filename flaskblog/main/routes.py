# BUILDING FILE - SUBSECTION MAIN #
# This file is used to define and create program pages.


# External extensions:
from flask import Blueprint, render_template, request, redirect, url_for
from googletrans import Translator
'''
(Legend)
From:
# flask: A micro web framework provides libraries to build web applications.
# googletrans: A library that implemented Google Translate API.

Import:
# Blueprint: A class providing structuring of the application.
# render_template: A function to render the html template (based on the Jinja2 engine).
# request: A function to process data sent from the client to the server.
# redirect: A function to redirect users to a specific URL.
# url_for: A function to generate a URL to a given endpoint.
# Translator: A class providing translations from Google Translate
'''


# Internal extensions:
from flaskblog import Locale, us, cz
from flaskblog.db_models import User, Post
from flaskblog.main.about_texts import texts, links
'''
(Legend)
From:
# flaskblog: The __init__.py file in the root directory.
# flaskblog.db_models: The db_models.py file in the root directory.
# flaskblog.main.about_texts: The about_texts.py file in the main folder in the root directory.

Import:
# Locale: A class providing language settings.
# us: An instance of the Locale class for the English language
# cz: An instance of the Locale class for the Czech language
# User: A class with defined columns for the users database table.
# Post: A class with defined columns for the posts database table.
# text: A list of texts for the about page.
# links: A list of links for the about page.
'''


# Page blueprint settings:
main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    '''
    Route function for creating a home page.
    
    :return: Home page.

    Legend:
    Decorator:
    # @main.route("/"): Defining the page address (by root directory).
    # @main.route("/home"): Defining the page address (by root directory).

    Create a variable with the page number:
    # request.args.get(): A method to access the URL parameter value.
    # 'page', 1, type=int: Page counter settings.

    Posts retrieving:
    # Post.query: Query for the Post database table.
    # .order_by(Post.date_posted.desc()): Sorting the result by date, descending.
    # .paginate(page=page, per_page=5): Setting the number of posts per page.

    Translation:
    # Locale.post_to_translate[:]: The contents of the post_to_translate list of the Locale class attribute.

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'main_home.html': Name of the html file (in the template directory).
    # posts=posts: Posts data.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    # translate=translate: The contents of the post_to_translate list of the Locale class attribute / None.
    '''

    # Create a variable with the page number:
    page = request.args.get('page', 1, type=int)

    # Posts retrieving:
    posts = Post.query\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)

    # Translation:
    translate = Locale.post_to_translate[:]
    if translate != [None]:
        Locale.post_to_translate = [None]

    # Page rendering:
    return render_template('main_home.html',
        posts=posts,
        language=Locale.current.language,
        translate=translate
    )


@main.route("/about")
def about(admin_username="Sudip2708"):
    '''
    Route function for creating an about page.

    :param admin_username: Username of the page administrator.
    :return: About page.


    Legend:
    Decorator:
    # @main.route("/about"): Defining the page address (by root directory).

    User verification:
    # User.query: Query for the User database table.
    # filter_by(): Search parameters.
    # first_or_404(): Return the first value found or raise a 404 error.

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'main_about.html': Name of the html file (in the template directory).
    # user=user: User data.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    # links=links: A list of links for the about page.
    # text=texts): A list of texts for the about page.
    '''

    # User verification:
    user = User.query.filter_by(username=admin_username).first_or_404()

    # Page rendering::
    return render_template('main_about.html',
        user=user,
        language=Locale.current.language,
        links=links,
        text=texts)


@main.route("/change_language")
def change_language():
    '''
    Route function to change page localization..

    :return: Change language.

    Legend:
    Decorator:
    # @main.route("/change_language"): Defining the page address (by root directory).

    Change page language:
    # Locale.current: The Locale class attribute for the current language.
    # us: An instance of the Locale class for the English language
    # cz: An instance of the Locale class for the Czech language

    Redirecting to the previous page:
    # redirect(request.headers.get("Referer")): Redirecting (redirect) to previous page (request.headers.get("Referer")).
    '''

    # Changing page language:
    if Locale.current == cz:
        Locale.current = us
    else:
        Locale.current = cz

    # Redirecting:
    return redirect(request.headers.get("Referer"))


@main.route("/translate/<int:post_id>")
def translate(post_id):
    '''
    Route function for post translation.

    :param post_id: The ID of the post.
    :return: Translation of the post.

    Legend:
    Decorator:
    # @main.route("/translate/<int:post_id>"): Defining the page address (by root directory).

    Post retrieving:
    # Post.query: Query for the Post database table.
    # get_or_404(post_id): Return the value (based on post ID) or raise a 404 error.

    Translator:
    # Translator(): A class providing translations from Google Translate

    Translation:
    # translator.translate(): Method of the Translator class for translation.
    # dest=Locale.current.language: Translation language (according to the current page language).
    # .text: Extracting the part with translated text.

    Transfer of translation:
    # Locale.post_to_translate: Pass the translation to the post_to_translate attribute of the Locale class.

    Redirecting:
    # redirect(url_for()): Redirecting (redirect) to the url (url_for).
    # 'posts.post', post_id=post.id: For post page ('posts.post') and post by ID (post_id=post.id).
    '''

    # Post retrieving:
    post = Post.query.get_or_404(post_id)

    # Translator:
    translator = Translator()

    # Translations:
    title_translation  = translator.translate(
        post.title,
        dest=Locale.current.language
    ).text

    content_translation  = translator.translate(
        post.content,
        dest=Locale.current.language
    ).text

    # Transfer of translation:
    Locale.post_to_translate = [post_id, title_translation, content_translation]

    # Redirecting:
    return redirect(url_for('posts.post', post_id=post.id))
