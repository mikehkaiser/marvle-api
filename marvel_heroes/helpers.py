#helper functions wraps

from functools import wraps
#this will require a user token from an authorized user to access the db
import secrets
from flask import request, jsonify
from marvel_heroes.models import User, Hero

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(" ")[1]
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            current_user_token = User.query.filter_by(token = token).first()
            print(token)
        except:
            owner = User.query.filter_by(token=token).first()
            if token != owner.token and secrets.compare_digest(token):
                return jsonify({'message': 'Invalid Token. Try again.'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

import decimal
from flask import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)