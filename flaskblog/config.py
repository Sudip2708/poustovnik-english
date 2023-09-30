# APPLICATION CONFIGURATION FILE #
# This file contains a class with basic configuration of the application.


# External extensions:
import json
'''
Import:
# json: Built-in module for transferring data as text over the network.
'''

# Loading JSON:
with open('instance/config.json') as config_file:
    '''
    # with open(): Opening, loading, and closing the JSON file.
    # 'instance/config.json': File path.
    # as config_file: Alias for the JSON dictionary
    # json.load(config_file): Loading the JSON dictionary.
    '''
    config = json.load(config_file)


class Config:
    '''
    Class with the basic configuration of the application.

    Contains the following:
    # SECRET_KEY: Encryption key used for application security.
    # SQLALCHEMY_DATABASE_URI: Path to the SQLAlchemy database.
    # MAIL_SERVER: E-mail server.
    # MAIL_PORT: E-mail port.
    # MAIL_USE_TLS: E-mail security type.
    # MAIL_USERNAME: E-mail login name.
    # MAIL_PASSWORD: E-mail password.
    # MAIL_DEFAULT_SENDER: E-mail default sender.
    '''

    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = config.get('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('MAIL_USERNAME')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = config.get('MAIL_DEFAULT_SENDER')


