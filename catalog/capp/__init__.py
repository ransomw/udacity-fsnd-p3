import os

from flask import Flask
from flask.ext.seasurf import SeaSurf

import config

_SETTINGS_ENV_VAR = 'FLASK_CATALOG_SETTINGS'

app = Flask(__name__)
if os.environ.get(_SETTINGS_ENV_VAR):
    app.config.from_envvar(_SETTINGS_ENV_VAR)
else:
    app.config.from_object(config)
csrf = SeaSurf(app)

# although a pep8 violation, this is recommended at
# http://flask.pocoo.org/docs/0.10/patterns/packages/
import capp.views
