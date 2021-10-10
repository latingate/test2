from flask import Flask, redirect, request, render_template, request, session, url_for, jsonify
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter

from gs_functions import *

app = Flask(__name__)


@app.route('/podcast')
def podcast_main():
    return render_template('podcast_main.html')


if __name__ == '__main__':
    # use the line below to run flask server directly (not recommended for production)
    app.run(host='0.0.0.0', port=5000, debug=True)
    # , use_reloader=False

    # use the line below to run flask through waitress server, and than run waitress_server.py from pycharm or directly from command line using: python waitress_server.py
    # app = Flask(__name__)
