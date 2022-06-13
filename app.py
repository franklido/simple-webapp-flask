import os
from flask import Flask
app = Flask(__name__)

frutto = os.environ.get('FRUTTO')

@app.route("/")
def main():
	return "Benvenuto. Che frutto ci piace oggi?"

@app.route("/scopriamolo")
def scopriamolo():
	return FRUTTO

if __name__ == "__main__":
	app.run()
