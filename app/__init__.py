from flask import Flask
from config import Config


# flask application instance. member of the app package. global variable
app = Flask(__name__)
app.config.from_object(Config)


from app import routes
