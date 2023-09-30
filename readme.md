# Hi there!
This is the source code of the application for the website www.poustovnicek.fun <br>
The application is built in Flask (Python) based on a YouTube video tutorial by Corey Schafer: <br>
https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

I thank Corey Schafer very much for that. <br>
I really liked his way of explaining things and I learned a lot. <br>
(This was my first project after completing a 3 month web development training.)

The main purpose of this application is to be a promotional material for the job search process.
However, they can also serve as study material for someone, and for these cases I tried to make it as readable as possible. <br>

The main change, compared to Corey's original version, is the localization into my native language (Czech).
I used Flask-Babel for localization and Googletrans for additional translation of the posts. <br>
(A quick note on Flask-Babel: After using Blueprints, I had to switch in the terminal to the application folder to working with it.)

Another change is to use PyJWT instead of ItsDangerous, to create a time token.
(ItsDangerous does not support JWS since version 2.0.)

The other changes are mainly of an appearance nature, and given that they do not affect the functionality of the program, I will not even mention them.

If you have any questions about this application, here is a link to my LinkedIN and I will be happy to help if I know: <br>
https://www.linkedin.com/in/dalibor-sova-51652b286/  <br>
Everything here is fully available to you.

I wish you a pleasant day and a wonderful life. <br>
Sudip2708
<br> 9.9.2023 <br> 


## What the web application allows:
- View already created posts from other users. <br> 
- View posts from a specific user. <br> 
- Log in and create your own posts. <br> 
- Edit and delete your own posts. <br> 
- Set your own profile picture. <br> 
- Have an email sent to you with a link to change your password. <br> 
- Change your password (after visiting the link from the email). <br> 
- Switch between Czech and English page environment. <br> 
- Translate posts that are in a different language. <br> 
- And, of course, mobile-friendly responsive behavior :-)

## Program tree-structure:
```
run.py - Application executable file.
readme.md - You are reading this file.
requirements.txt - List of pip installs for a virtual environment.
```

#### instance /     

```
(folder for the database file)
site.dt - The database file.
```

#### flaskblog /     

```
(the main folder of the application)
__init__.py - Application initialization file.
config.py - Application configuration file.
models.py - Module with classes for creating database tables.
babel.cfg - Babel configuration file to initialize page translation (can be deleted).
messages.pot - Extraction of all marked texts for translation (can be deleted).
```

#### flaskblog / main /
```
(a folder with blueprints to display main and unclassified pages)
__init__.py - Blueprint folder initialization file.
about_text.py - File with text and links for the about page.
routes.py - File for building pages.
```

#### flaskblog / users /
```
(a folder with blueprints to display user pages)
__init__.py - Blueprint folder initialization file.
routes.py - File for building pages.
forms.py - File for page forms.
utils.py - File for additional features..
```

#### flaskblog / posts /

```
(a folder with blueprints to display post pages)
__init__.py - Blueprint folder initialization file.
routes.py - File for building pages.
forms.py - File for page forms.
```

#### flaskblog / errors /
```
(a folder with blueprints to display error pages)
__init__.py - Blueprint folder initialization file.
handlers.py - File for building pages.
```

#### flaskblog / static /
```
(a static folder)
main.css - CSS file for additional configuration of the page appearance (the main one is provided by bootstrap).
favicon.ico - Image to display in the site tab.
```

#### flaskblog / static / profile_pic /
```
(a folder for users' profile pictures)
default.jpg - Default profile picture.
```

#### flaskblog / templates /
```
(a folder for html documents)
layout.html - Template for all other pages.
layout_side_panel.html - Page for the side panel (layout extension for better transparency).
layout_side_panel_old.html - Page for the original side panel (extending the side panel).
main_about.html - Page about this app.
main_home.html - Post listing page.
posts_create_post.html - Post creation page.
posts_post.html - Post creation page.
posts_user_posts.html - Page to display posts from a specific user.
users_account.html - User account management page.
users_login.html - Login page.
users_register.html - User registration page.
users_reset_request.html - Page to generate and send a password reset token.
users_reset_token.html - Password change page (after receiving the token).
users_create_post.html - The post creation page.
users_post.html - Post creation page.
users_user_posts.html - Page to display posts from a specific user.
```

#### flaskblog / templates / errors /

```
(a folder for html files reporting the error)
403.html - Page for 403 (Access Denied) error.
404.html - Page for a 404 error (Bad Link/Page Not Found).
500.html - Page for error 500 (server error).
```

#### flaskblog / translations / cs / LC_MESSAGES /

```
(a folder for Czech translation of pages)
messages.po - File for translation of individual texts.
messages.mo - Generated binary file for translating the page.
```


## List of pip installs:
```
$ pip install flask 
(website creation, version 2.3.3)

$ pip install flask-sqlalchemy 
(database work, version 3.0.5)

$ pip install flask-bcrypt 
(encryption, version 1.0.1)

$ pip install flask-login 
(login management, version 0.6.2)

$ pip install pyjwt 
(JWT web tokens, version 2.8.0)

$ pip install flask_wtf 
(web forms, version 1.1.1)

$ pip install flask-mail 
(setting up and using mail, version 0.9.1)

$ pip install email_validator 
(email verification, version 2.0.0.post2)

$ pip install Pillow 
(image processing, version 10.0.0)

$ pip install Flask-Babel 
(site localization, version 3.1.0)

$ pip install googletrans==3.1.0a0 
(translation of posts, version 3.1.0a0 )
```

## Helpful links:

Flask: <br>
https://flask.palletsprojects.com/en/2.3.x/api/#application-object

Flask-SQLAlchemy: <br>
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/api/#flask_sqlalchemy.SQLAlchemy

Flask-Bcrypt: <br>
https://flask-bcrypt.readthedocs.io/en/1.0.1/

Flask-Login: <br>
https://flask-login.readthedocs.io/en/latest/

Flask-Pyjwt: <br>
https://pyjwt.readthedocs.io/en/latest/usage.html

Flask-WTF: <br> 
https://flask-wtf.readthedocs.io/en/1.1.x/

Flask-Mail: <br>
https://pythonhosted.org/Flask-Mail/

Email validator: <br>
https://pypi.org/project/email-validator/

Pillow: <br>
https://pillow.readthedocs.io/en/stable/

Flask-Babel: <br>
https://python-babel.github.io/flask-babel/#gettext-functions

Googletrans: <br>
https://pypi.org/project/googletrans/3.1.0a0/