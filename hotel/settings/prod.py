from .base import *
from .setting_utils import _init_app_db

# MySQL configuration
DATABASE = {
    'MYSQL_HOST': 'db.michaeldpalmer.com',
    'MYSQL_DB': 'hotel',
    'MYSQL_USER': 'hotel',
    'MYSQL_PASSWORD': 'ZfDh3wpDRBZbmUmC'
}

_init_app_db(mysql, app, DATABASE)

registered_tables = ['asset']
