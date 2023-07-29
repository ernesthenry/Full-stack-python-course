import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO DONE: IMPLEMENT DATABASE URL

database_name = 'fyyur'
database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', '123', 'localhost:5432', database_name)
SQLALCHEMY_DATABASE_URI = database_path

