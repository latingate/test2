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


@app.route("/edit_record/<id>")
def edit_record(id):
    db = open_mongodb_connection()

    filter_json = {
        "_id": id
    }

    sort_by = [('_id', 1)]

    results = db.find(
        filter=filter_json,
        sort=sort_by
    )
    return render_template('edit_record.html', id=id)


app.run(debug=True)
