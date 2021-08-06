#helper functions wraps

from functools import wraps
#this will require a user token from an authorized user to access the db
import secrets
from flask import request, jsonify

def token_required(flask_function):
    @wraps(flask_function)
    def decorated(*args, **kwargs):
        pass