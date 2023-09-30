# FILE FOR ADDITIONAL FUNCTIONS ASSOCIATED WITH USERS DATA #
# This file is used to define functions for working with user data.


# External extensions:
from flask import url_for, current_app
from flask_mail import Message
from flask_babel import lazy_gettext
from PIL import Image
import os
import secrets
'''
(Legend)
From:
# flask: A micro web framework provides libraries to build web applications.
# flask_mail: A Flask extension that provides email management and sending.
# flask_babel: A Flask extension that provides internationalization and localization.
# PIL: A Flask extension that provides a library for images processing.

Import:
# url_for: A function for generate an URL (for a given endpoint).
# current_user: A function returns the proxy of the logged user.
# Message: A class providing creation of e-mail messages.
# lazy_gettext: A function to mark text for lazy translation (translation is delayed until needed).
# Image: A class providing picture editing.
# os: A module that provides operating system-dependent functionality.
# secrets: A module  for generating cryptographically strong random numbers.
'''


# Internal extensions:
from flaskblog import mail
'''
(Legend)
From:
# flaskblog: 

Import:
# mail: Instance of the Mail class for sending emails
'''


def save_picture(form_picture):
    '''
    A functions for processing and saving a profile picture.

    :param form_picture: The picture received from the page form.
    :return: Name of edited picture.

    Legend:
    New image name and path:
    # secrets.token_hex(8): Module for generating hex numbers.
    # _,: Placeholder for an unused variable.
    # os.path.splitext(): Module for splitting the file name and its extension.
    # form_picture.filename: Filename from the picture received from the page form
    # os.path.join: Module for joining path segments.
    # current_app.root_path: The path to the root directory of the application.
    # 'static/profile_pictures': The folder where the image is located.

    Image resizing:
    # Image.open(form_picture): Create an instance of the Image class and open the image for editing.
    # thumbnail(required_size): A method to resize an image.
    # save(new_picture_path): A method for saving images.
    '''

    # New image name and path:
    radom_eight_bit_number = secrets.token_hex(8)
    _, picture_extension = os.path.splitext(form_picture.filename)
    new_picture_name = radom_eight_bit_number + picture_extension
    new_picture_path = os.path.join(current_app.root_path, 'static/profile_pictures', new_picture_name)

    # Image resizing:
    required_size = (125, 125)
    image_to_resize = Image.open(form_picture)
    image_to_resize.thumbnail(required_size)
    image_to_resize.save(new_picture_path)

    return new_picture_name


def send_reset_email(user):
    '''
    A function to send an email with a time token to change the password.

    :param user: The user who requested it.
    :return: Sent email with time token.

    Legend:
    Token creation:
    # user.get_reset_token(): Method of the User class to create a time token.

    Message instance:
    # Message(): A class providing creation of e-mail messages.
    # lazy_gettext("Password Reset Request"): Email name with translation marking for Babel.
    # recipients=[user.email]: List of recipients (only one here).

    Message body:
    # url_for(): A function for generate an URL (for a given endpoint).
    # _external=True: Specification that we need an absolute URL (and not a relative URL).
    # message.body: Class attribute for message body content.
    # mail.send(message): Calling an instance of the Mail class to send email.
    '''

    # Token creation:
    token = user.get_reset_token()

    # Message instance:
    message = Message(lazy_gettext("Password Reset Request"), recipients=[user.email])

    # Message body:
    message_intro = lazy_gettext("To reset your password, visit the following link:")
    message_ling_with_token = url_for('users.reset_token', token=token, _external=True)
    message_ending = lazy_gettext("If you did not make this request "
                                  "then simply ignore this email and no changes will be made.")
    message.body = message_intro \
                   + "\n" \
                   + message_ling_with_token \
                   + "\n\n" \
                   + message_ending

    # Message sending:
    mail.send(message)

