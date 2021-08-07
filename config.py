# used to set up the connection to the database

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY="Justice Friends ASSEMBLE"
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS=False