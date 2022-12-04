#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(self):
    """Method to handle app.teardown_appcontext"""
    self.storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    """Function that display a HTML page"""
    return render_template("7-states_list.html", states=storage.all("State"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
