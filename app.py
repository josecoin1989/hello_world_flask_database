from flask import Flask
from controller.ctrl_database import database
from controller.ctrl_test import  test


app = Flask(__name__)
app.register_blueprint(database)
app.register_blueprint(test)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":

    app.run(port=8888)