from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    s = "This is Gal's server"
    s += "<br/>Other routes:"
    s += "<br/><a href='/gal'>/gal</a>"
    s += "<br/><a href='/test'>/test</a>"
    return s


@app.route("/gal")
def gal():
    return "This is /gal route"


admin_name = 'Gal Sarig'


@app.route("/test")
def template():
    first_name = 'Gal'
    last_name = 'Sarig'
    return render_template('flask_test.html', name=first_name + ' ' + last_name, admin_name=admin_name)


app.run(debug=True)
