 
from flask import Flask
# from .config import DevConfig
from flask_bootstrap import Bootstrap
from .config import config_options

bootstrap =Bootstrap()

def create_app(config_name):
    #initializing application
    app = Flask(__name__)

    #create the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)

    
    return app



# #setting up configurations
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')
# from app import views