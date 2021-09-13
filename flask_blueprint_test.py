from flask import Blueprint

flask_blueprint_test = Blueprint('flask_blueprint_test', __name__)


@flask_blueprint_test.route('/blueprint1')
def simple_page():
    return render_template('this is test #1 (blueprint example in flask)')


@flask_blueprint_test.route('/blueprint2')
def simple_page2():
    return 'this is test #2 (blueprint example in flask)'
