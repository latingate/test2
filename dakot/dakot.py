from flask import Flask, redirect, request, render_template, request, session, url_for, jsonify
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter

from gs_functions import *


@app.route('/podcast')
def podcast_main():
    return render_template('podcast_main.html')
