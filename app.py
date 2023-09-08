from flask import Flask
from controllers.library_controllers import library_blueprint
#there is an issue here

app = Flask(__name__)
app.register_blueprint(library_blueprint)