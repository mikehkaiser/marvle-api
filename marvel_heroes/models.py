#used to set the template for the database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date, datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy() #link to init
ma = Marshmallow() #link to init

login_manager = LoginManager() #link to init
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(150))
    token = db.Column(db.String, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hero = db.relationship('Hero', backref='owner', lazy=True)

    def __init__(self, email, password, name, id='', token=''):
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password)
        self.name = name
        self.token = self.set_token(24)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self, length):
        return secrets.token_hex(length)

class Hero(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    alter_ego = db.Column(db.String(150))
    description = db.Column(db.String(300))
    comics_appeared_in = db.Column(db.String(300))
    super_power = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    owner_token = db.Column(db.String, db.ForeignKey('user.token'))

    def __init__(self, name, alter_ego, description, comics_appeared_in, super_power, owner_token, id=''):
        self.id = self.set_id()
        self.name = name
        self.alter_ego = alter_ego
        self.description = description
        self.comics_appeared_in = comics_appeared_in
        self.super_power = super_power
        self.owner_token = owner_token

    def set_id(self):
        return (secrets.token_urlsafe())

class HeroSchema(ma.Schema):
    class Meta:
        fields = ['id','name','alter_ego','description','comics_appeared_in','super_power','date_created','owner_token']

hero_schema=HeroSchema()
heroes_schema=HeroSchema(many=True)