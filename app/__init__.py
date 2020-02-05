from flask import Flask

# flask application instance. member of the app package. global variable
app = Flask(__name__)

from app import routes
