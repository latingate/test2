from flask import Flask, Blueprint, redirect, request, render_template, request, session, url_for, jsonify

flask_blueprint_test = Blueprint('flask_blueprint_test', __name__)


@flask_blueprint_test.route('/blueprint1')
def simple_page():
    return render_template('this is test #1 (blueprint example in flask)')


@flask_blueprint_test.route('/blueprint2')
def simple_page2():
    return 'this is test #2 (blueprint example in flask)'

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
