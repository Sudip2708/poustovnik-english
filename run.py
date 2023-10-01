# EXECUTABLE PROGRAM FILE #
# This file is used to run the program.


# Application import:
from flaskblog import create_app

# Application initialization::
app = create_app()

# Starting the application (debug mode activation/deactivation):
if __name__ == '__main__':
    app.run(debug=True)
