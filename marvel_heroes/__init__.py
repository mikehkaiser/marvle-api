from flask import Flask
from flask_migrate import Migrate
from flask_wtf.recaptcha.widgets import JSONEncoder
from .site.routes import site
from .api.routes import api
from .authentication.routes import auth
from .models import db, login_manager, User, ma
from config import Config
from flask_cors import CORS
from .helpers import JSONEncoder

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

db.init_app(app)
ma.init_app(app)
CORS(app)

login_manager.init_app(app)

login_manager.login_view='auth.signin'

migrate = Migrate(app, db)

app.json_encoder = JSONEncoder