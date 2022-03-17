from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()




def create_app(config_name):

    app = Flask(__name__)

    # creating app configurations
    app.config.from_object(config_options[config_name])


    # register blueprint
    from .views import views as main_blueprint
    app.register_blueprint(main_blueprint)

    # initialize flask extensions
    db.init_app(app)
    CORS(app)


    return app
