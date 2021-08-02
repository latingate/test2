from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    s = "This is Gal's server"
    s += "<br/>Other routes:"
    s += "<br/><a href='/gal'>/gal</a>"
    s += "<br/><a href='/template'>/template</a>"
    return s


@app.route("/gal")
def gal():
    return "This is /gal route"


@app.route("/template")
def template():
    return render_template('flask_test.html')


app.run(debug=True)
