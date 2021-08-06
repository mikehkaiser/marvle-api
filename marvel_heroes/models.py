#used to set the template for the database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import uuid
from flask_sqlalchemy.model import Model
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy() #link to init
ma = Marshmallow() #link to init

login_manager = LoginManager() #link to init

class User(db.Model, UserMixin):
    pass


class Hero(db.Model):
    pass

class HeroSchema(ma.schema):
    class Meta:
        fields = ['id','name','descriptions','comics_appeared_in','super_power','date_created','owner']

hero_schema=HeroSchema()
heroes_schema=HeroSchema(many=True)