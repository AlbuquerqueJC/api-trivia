import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Setup Database
DATABASE_SETUP = {
    "database_name_production": "trivia",
    "database_name_test": "trivia_test",
    "user_name": "jca",  # default postgres user name
    "password": "jca",  # if applicable. If not type in None
    "port": "localhost:5432"  # default postgres port
}

# Construct Database URI
database_path = "postgres://{}:{}@{}/{}"\
    .format(DATABASE_SETUP["user_name"],
            DATABASE_SETUP["password"],
            DATABASE_SETUP["port"],
            DATABASE_SETUP["database_name_production"])

SQLALCHEMY_DATABASE_URI = database_path
