from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from config import config_options



bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

# Initializing application
    app = Flask(__name__)

   
# Creating the app configurations
    app.config.from_object(config_options[config_name])

# Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')



    # setting config
    from .requests import configure_request
    configure_request(app)

    return app