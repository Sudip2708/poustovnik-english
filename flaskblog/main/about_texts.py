# FILE WITH TEXTS AND LINKS FOR THE ABOUT PAGE #
# This file is used to group texts and links for the about page.


# External extensions:
from flask_babel import lazy_gettext
'''
(Legend)
From:
# flask_babel: A Flask extension that provides internationalization and localization.

Import:
# lazy_gettext: A function to mark text for lazy translation (translation is delayed until needed).
'''


# Text list:
texts = [

    (lazy_gettext("...and thank you Corey!"),
     lazy_gettext("This pages are based on a YouTube video tutorial by Corey Schafer. "
     "They are made in Flask and they are my first real project and also real proof of Corey great teaching skills.")),

    (lazy_gettext("About me"),
     lazy_gettext("I am quite newbie in the programming world. "
     "I've been studying Python for about a year and a half, and recently I completed a three-month course on creating web applications. "
     "So I was looking for some project to combine and practice new skills and found this. "
     "And I was perfect.")),

    (lazy_gettext("Purpose of this page"),
     lazy_gettext("The main purpose of this page is just to present my current level to a potential employer and apart the fact I learned a lot by doing them they don't have a deeper meaning.")),

    (lazy_gettext("Sharing is caring"),
     lazy_gettext("Anything here is free to use. "
     "And if you have some question about this page or you have a job offer don't hesitate to ask. "
     "My email is in linkedin profile :-)")),

    (lazy_gettext("Wish you all Wonderful Life..."),
     "9. 9. 2023"),
]


# List of links:
links = [

    (lazy_gettext("Tutorial by Corey Schafer"),
     'https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH',
     '_blank',
     lazy_gettext("(link to Corey Schafer youtube tutorial)")),

    (lazy_gettext("Full code description (Czech)"),
     'https://github.com/Sudip2708/poustovnik-rozbor.git',
     '_blank',
     lazy_gettext("(code analysis in Czech)")),

    (lazy_gettext("Code in readable form (English)"),
     'https://github.com/',
     '_blank',
     lazy_gettext("(code in English transcribed into readable notation)")),

    (lazy_gettext("My LinkedIn"),
     'https://www.linkedin.com/in/dalibor-sova-51652b286/',
     '_blank',
     lazy_gettext("(link to my LinkedIn)")),
]
