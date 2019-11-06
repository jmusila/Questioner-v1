"""
 App module to bring together the whole app.

"""

# Standard library import
import os
from datetime import timedelta

# Third party imports
from flask import Flask

# Local imports
from .api.v1.routes import api
from instance.config import app_config



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    api.init_app(app)
    app.url_map.strict_slashes = False 

    from .api.v1.routes import version1 as v_1
    app.register_blueprint(v_1)

    return app