from main.app import app
# https://flask.palletsprojects.com/en/stable/deploying/gunicorn/

application = app.server # Dash flask server for WSGI
