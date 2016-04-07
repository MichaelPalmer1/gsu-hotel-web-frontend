

# this sets the DB values and inits the app
def _init_app_db(mysql, app, database):

    for field_name, value in database.items():
        app.config[field_name] = value

