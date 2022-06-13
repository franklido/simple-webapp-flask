import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
	return "Benvenuto"

@app.route("/come stai?")
def scopriamolo():
	return "La pomme est rouge"

if __name__ == "__main__":
	app.run()
