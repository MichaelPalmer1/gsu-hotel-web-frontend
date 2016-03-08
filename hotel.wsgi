# /usr/bin/python
# import sys
# import logging
import os
from hotel import app

# logging.basicConfig(stream=sys.stderr)
# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# from hotel import app
app.config.from_object(os.environ['FLASK_SETTINGS_MODULE'])
app.secret_key = 'secret'

if app.config['DEBUG']:
    app.run(debug=True, port=8000)
