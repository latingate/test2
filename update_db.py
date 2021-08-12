from flask import Flask, redirect, request, render_template, request, session, url_for, jsonify
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from pymongo import MongoClient
import json
import os

from gs_functions import *

app = Flask(__name__)

dropzone = Dropzone(app)


@app.route("/")
def list_records():
    db = open_mongodb_connection()
    cursor = db.find({})
    return render_template('list_records.html', cursor=cursor)


app.run(debug=True)
