from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

#initializing application
app = Flask(__name__)

 # Creating the app configurations
app.config.from_object(config_options[config_name])

# #setting up configurations
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap.init_app(app)

# from app import views
return app
