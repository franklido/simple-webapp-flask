import os
from flask import flask
app = flask(__name__)

@app.route("/")
def main():
	return "Welcome!"

@app.route("/mela")
def mela():
	return "Le pomme est rouge"

if __name__ == "__main__":
	app.run()
