from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()

"""
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) 


notes = []

#to comment after returning to normal
@app.route("/", methods=["GET", "POST"])
def index():
    headline = "Hello !"
    
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    
    return render_template("index.html", headline=headline, notes = notes)


@app.route("/", methods=["GET", "POST"])
def index():
    session["notes"] = notes
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("index.html", notes=session["notes"])


@app.route("/david")
def david():
    return "Hello David!"

#to comment after returning to normal

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello {name}!<h1>"



@app.route("/bye")
def bye():
    headline = "GoodBye!"
    return render_template("index.html", headline=headline)

@app.route("/more")
def more():
    headline = "Second page !"
    return render_template("more.html", headline = headline)

@app.route("/hi", methods=["GET", "POST"])
def hi():
    if request.method == "GET":
        return "Please submit the form first"
    name = request.form.get("name")
    return render_template("hello.html", name = name)

"""