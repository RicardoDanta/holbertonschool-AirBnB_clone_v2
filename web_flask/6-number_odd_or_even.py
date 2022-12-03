#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Function that return Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function that return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function that return C followed
    by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def p_text(text="is cool"):
    """Function that return C followed
    by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def n_number(n):
    """Function that return a text
    but only if the variable is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Function that displays a HTML page
    but only if the variable is an integer"""
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Function that return a text
    but only if the variable is an integer"""
    if (n % 2) == 0:
        addeven = "Number: {} is even".format(n)
    else:
        addeven = "Number: {} is odd".format(n)
        return render_template("5-numer_add_or_even.html", addeven)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
