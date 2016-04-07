import sys
import os
from hotel import app as application

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('FLASK_SETTINGS_MODULE', 'hotel.settings.prod')
application.config.from_object(os.environ['FLASK_SETTINGS_MODULE'])

if application.config['DEBUG']:
    application.run(port=8000, debug=True)
else:
    application.run(host='0.0.0.0', port=80)
