# FILE FOR BUILDING WEB PAGES - POSTS SUBSECTION #
# This file is used to define and create web pages of the application.


# External extensions:
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import current_user, login_required
from flask_babel import lazy_gettext
'''
(Legend)
From:
# flask: A micro web framework provides libraries to build web applications.
# flask_login: A Flask extension that provides user session management.
# flask_babel: A Flask extension that provides internationalization and localization.

Import:
# Blueprint: A class providing structuring of the application.
# render_template: A function to render the html template (based on the Jinja2 engine).
# request: A function to process data sent from the client to the server.
# redirect: A function to redirect users to a specific URL.
# url_for: A function to generate a URL to a given endpoint.
# flash: A function to display an informational messages.
# abort: A function to prematurely abort a request with an error code.
# current_user: A function returns the proxy of the logged user.
# login_required: A function to verify if the user is login.
# lazy_gettext: A function to mark text for lazy translation (translation is delayed until needed).
'''


# Internal extensions:
from flaskblog import Locale, db
from flaskblog.db_models import Post, User
from flaskblog.posts.forms import PostForm
'''
(Legend)
From:
# flaskblog: __init__.py file in the root directory.
# flaskblog.db_models: The db_models.py file in the root directory.
# flaskblog.posts.forms: The forms.py file in the posts folder in the root directory.

Import:
# Locale: A class providing language settings.
# db: An instance of SQLAlchemy class (used for databases).
# Post: A class with defined columns for the posts database table.
# User: A class with defined columns for the users database table.
# PostForm: A class to manage the form data on the page (here for adding a new post).
'''


# Page blueprint settings:
posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    '''
    Route function for creating an adding a new post page.

    :return: Adding a new post page.

    Legend:
    Decorator:
    # @users.route("/post/new"): Defining the page address (by root directory).
    # methods=['GET', 'POST']: Defining the methods used for the page.
    # @login_required: Permission for logged users only.

    Entry form validation:
    # PostForm(): A class to manage the form data on the page (here for adding a new post).
    # validate_on_submit(): A shortcut for is_submitted() and validate().

    Entering data into database:
    # post: An instance of the Post class for post data.
    # db.session.add(post): Adding data to the database.
    # db.session.commit(): Commit changes to the database.

    Info message:
    # flash(): A function for display an informational messages.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # 'success': Message category.

    Redirecting:
    # redirect(url_for('main.home')): Redirecting (redirect) to the url (url_for) for home page ('main.home').

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'posts_create_post.html': Name of the html file (in the template directory).
    # title='New Post': Page title.
    # form=form: Page form.
    # legend=lazy_gettext('New Post'): The name of the page.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).

    '''

    # Entry form validation:
    form = PostForm()
    if form.validate_on_submit():

        # (entering data into database):
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
            language=Locale.current.language
        )
        db.session.add(post)
        db.session.commit()

        # (info message & redirecting):
        flash(lazy_gettext("Your post has been created!"), 'success')
        return redirect(url_for('main.home'))

    # Page rendering:
    return render_template(
        'posts_create_post.html',
        title=lazy_gettext('New Post'),
        form=form,
        language=Locale.current.language
    )


@posts.route("/post/<int:post_id>")
def post(post_id):
    '''
    Route function for creating a selected post page.

    :param post_id: The ID of the post.
    :return: Selected post page.

    Legend:
    Decorator:
    # @users.route("/post/<int:post_id>"): Defining the page address (by root directory).

    Post retrieving:
    # Post.query: Query for the Post database table.
    # get_or_404(post_id): Return the value (based on post ID) or raise a 404 error.

    Translation:
    # Locale.post_to_translate[:]: The contents of the post_to_translate list of the Locale class attribute.

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'posts_post.html': Name of the html file (in the template directory).
    # title=post.title: Page title.
    # post=post: Post.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    # translate=translate: The contents of the post_to_translate list of the Locale class attribute / None.
    '''

    # Post retrieving:
    post = Post.query.get_or_404(post_id)

    # Translation:
    translate = Locale.post_to_translate[:]
    if translate != [None]:
        Locale.post_to_translate = [None]

    # Page rendering:
    return render_template(
        'posts_post.html',
        title=post.title,
        post=post,
        language=Locale.current.language,
        translate=translate
    )


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    '''
    Route function for creating a post edit page.

    :param post_id: The ID of the post.
    :return: Post edit page.

    Legend:
    Decorator:
    # @users.route("/post/<int:post_id>/update"): Defining the page address (by root directory).
    # methods=['GET', 'POST']: Defining the methods used for the page.
    # @login_required: Permission for logged users only.

    Post retrieving:
    # Post.query: Query for the Post database table.
    # get_or_404(post_id): Return the value (based on post ID) or raise a 404 error.

    User authentication:
    # post.author: Author of the post.
    # current_user: A function returns the proxy of the logged user.
    # abort(403): Process aborted with error 403.

    Entry form validation:
    # PostForm(): A class to manage the form data on the page (here for adding a new post).
    # validate_on_submit(): A shortcut for is_submitted() and validate().

    Entering data into database:
    # post.xxx: Data from the post's database table.
    # form.xxx.data: Page form data.
    # db.session.commit(): Commit changes to the database.

    Info message:
    # flash(): A function for display an informational messages.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # 'success': Message category.

    Redirecting:
    # redirect(url_for()): Redirecting (redirect) to the url (url_for).
    # 'posts.post', post_id=post.id: For post page ('posts.post') and post by ID (post_id=post.id).

    Data pre-filling:
    # request.method == 'GET': A condition to check for data retrieved.
    # form.xxx.data: Page form data.
    # post.xxx: Data from the post's database table.

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'posts_create_post.html': Name of the html file (in the template directory).
    # title=lazy_gettext('Update Post'): Page title.
    # form=form: Page form.
    # legend=lazy_gettext('Update Post'): The name of the page.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    '''

    # Post retrieving:
    post = Post.query.get_or_404(post_id)

    # User authentication:
    if post.author != current_user:
        abort(403)

    # Entry form validation:
    form = PostForm()
    if form.validate_on_submit():

        # (entering data into database):
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()

        # (info message & redirecting):
        flash(lazy_gettext("Your post has been updated!"), 'success')
        return redirect(url_for('posts.post', post_id=post.id))

    # Data pre-filling:
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    # Page rendering:
    return render_template(
        'posts_create_post.html',
        title=lazy_gettext('Update Post'),
        form=form,
        language=Locale.current.language
    )


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    '''
    Route function for delete post.

    :param post_id: The ID of the post.
    :return: Home page.

    Legend:
    Decorator:
    # @users.route("/post/<int:post_id>/delete"): Defining the page address (by root directory).
    # methods=['POST']: Defining the methods used for the page.
    # @login_required: Permission for logged users only.


    Post retrieving:
    # Post.query: Query for the Post database table.
    # get_or_404(post_id): Return the value (based on post ID) or raise a 404 error.

    User authentication:
    # post.author: Author of the post.
    # current_user: A function returns the proxy of the logged user.
    # abort(403): Process aborted with error 403.

    Deleting post:
    # db.session.delete(post): Deleting a post from the database.
    # db.session.commit(): Commit changes to the database.

    Info message:
    # flash(): A function for display an informational messages.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # 'success': Message category.

    Redirecting:
    # return redirect(url_for('main.home')):
    '''

    # Post retrieving:
    post = Post.query.get_or_404(post_id)

    # User authentication:
    if post.author != current_user:
        abort(403)

    # Deleting post:
    db.session.delete(post)
    db.session.commit()

    # Info message & Redirecting:
    flash(lazy_gettext("Your post has been deleted!"), 'success')
    return redirect(url_for('main.home'))


@posts.route("/user/<string:username>")
def user_posts(username):
    '''
    Route function for creating a page with user posts.

    :param username: Username.
    :return: Page with user posts.

    Create a variable with the page number:
    # request.args.get(): A method to access the URL parameter value.
    # 'page', 1, type=int: Page counter settings.

    User verification:
    # User.query: Query for the User database table.
    # filter_by(): Search parameters.
    # first_or_404(): Return the first value found or raise a 404 error.

    Posts retrieving:
    # Post.query: Query for the Post database table.
    # .filter_by(author=user):  Search parameters.
    # .order_by(Post.date_posted.desc()): Sorting the result by date, descending.
    # .paginate(page=page, per_page=5): Setting the number of posts per page.

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'posts_user_posts.html': Name of the html file (in the template directory).
    # posts=posts: Posts data.
    # user=user: User data.
    # language=Locale.current.language: The current page language (based on the language attribute in the Locale class).
    '''

    # Create a variable with the page number:
    page = request.args.get('page', 1, type=int)

    # User verification:
    user = User.query.filter_by(username=username).first_or_404()

    # Posts retrieving:
    posts = Post.query\
        .filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)

    # Page rendering:
    return render_template(
        'posts_user_posts.html',
        posts=posts,
        user=user,
        language=Locale.current.language
    )