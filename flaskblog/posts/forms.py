# FILE TO CREATE DATABASE LINKED WEB FORMS - POSTS SUBSECTION #
# This file is used to define and connect the web form fields with database table.


# External extensions:
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_babel import lazy_gettext
'''
(Legend)
From:
# flask_wtf: A Flask extension that integrates the WTForms library.
# wtforms: A library that provides flexible web form rendering.
# wtforms.validators: Validator classes for form fields.
# flask_babel: A Flask extension that provides internationalization and localization.

Import:
# FlaskForm: A class for web forms with csrf protection.
# StringField: A class for the base text field.
# SubmitField: A class for submitting web form data.
# TextAreaField: A class for a multiline text field.
# DataRequired: A class for verifying whether a field is filled.
# lazy_gettext: A function to mark text for lazy translation (translation is delayed until needed).
'''


class PostForm(FlaskForm):
    '''
    Class with form definitions for a new post page.

    :param FlaskForm: Class for web forms with csrf protection.

    Legend:
    # StringField(): A class for the base text field.
    # TextAreaField(): A class for a multiline text field.
    # SubmitField(): A class for submitting web form data.
    # lazy_gettext(): A function to mark text for lazy translation (translation is delayed until needed).
    # DataRequired(): A class for verifying whether a field is filled.
    '''

    title = StringField(
        lazy_gettext("Title"),
        validators=[DataRequired()]
    )

    content = TextAreaField(
        lazy_gettext("Content"),
        validators=[DataRequired()]
    )

    submit = SubmitField(
        lazy_gettext("Post")
    )
