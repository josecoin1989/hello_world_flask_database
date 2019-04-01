"""
Author: José Antonio Domínguez González
Date: 31/03/2019
"""

from flask import Flask
from controller.ctrl_database import database
from controller.ctrl_test import test

# Declare the flask app
app = Flask(__name__)

# Register the end-points in the app
app.register_blueprint(database)
app.register_blueprint(test)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":

    # Start the app in the port 8888
    app.run(port=8888)