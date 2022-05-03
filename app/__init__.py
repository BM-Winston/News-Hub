from flask import Flask
from config import config_options


def create_app(config_name) :

    app = Flask(__name__)


    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)


#To register the blueprintc
    from .main import main as main_blueprint



    return app