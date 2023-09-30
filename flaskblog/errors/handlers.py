# BUILDING FILE - HANDLERS SUBSECTION #
# This file is used to define and create error reporting pages.


# External extensions:
from flask import Blueprint, render_template
'''
(Legend)
From:
# flask: A micro web framework provides libraries to build web applications.

Import:
# Blueprint: A class providing structuring of the application.
# render_template: A function to render the html template (based on the Jinja2 engine).
'''


# Page blueprint settings:
errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    '''
    Route function for creating a not found error page (error 404).

    :param error: Raised error.
    :return: Page for raised error.

    Legend:
    Decorator:
    # @errors.app_errorhandler(404):

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'errors/404.html': Name of the html file (in the template directory).
    # 404: Error number.
    '''

    # Page rendering:
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    '''
    Route function for creating a permission error page (error 403).

    :param error: Raised error.
    :return: Page for raised error.

    Legend:
    Decorator:
    # @errors.app_errorhandler(403):

    Page rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'errors/403.html': Name of the html file (in the template directory).
    # 403: Error number.
    '''

    # Page rendering:
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    '''
    Route function for creating a server error page (error 500).

    :param error: Raised error.
    :return: Page for raised error.

    Legend:
    Decorator:
    # @errors.app_errorhandler(500):

    PPage rendering:
    # render_template(): A function for rendering of an html template (based on the Jinja2 engine).
    # 'errors/500.html': Name of the html file (in the template directory).
    # 500: Error number.
    '''

    # Page rendering:
    return render_template('errors/500.html'), 500

