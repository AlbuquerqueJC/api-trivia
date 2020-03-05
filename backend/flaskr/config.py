import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_TRACK_MODIFICATIONS = False
database_name = "trivia_test"
database_user = "jca"
database_path = "postgres://{}:{}@{}/{}".format(database_user, database_user, 'localhost:5432', database_name)
SQLALCHEMY_DATABASE_URI = database_path
