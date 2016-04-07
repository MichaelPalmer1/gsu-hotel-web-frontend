from .base import *
from .setting_utils import _init_app_db

# MySQL configuration
DATABASE = {
    'MYSQL_HOST': 'localhost',
    'MYSQL_DB': 'hotel',
    'MYSQL_USER': 'root',
    'MYSQL_PASSWORD': ''
}

DEBUG = True

_init_app_db(mysql, app, DATABASE)

registered_tables = ['asset']
