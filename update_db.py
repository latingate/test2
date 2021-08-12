from flask import Flask, redirect, request, render_template, request, session, url_for, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from dataclasses import dataclass
import json
import os

from gs_functions import *

app = Flask(__name__)


@dataclass
class User_db:
    _id: str
    first_name: str
    last_name: str
    initials: str
    age: int
    pics: dict


@app.route("/")
def list_records():
    db = open_mongodb_connection()
    cursor = db.find({})
    return render_template('list_records.html', cursor=cursor)


@app.route("/edit_record/<user_id>")
def edit_record(user_id):
    db = open_mongodb_connection()

    filter_json = {
        "_id": ObjectId(user_id)
    }

    sort_by = [('_id', 1)]

    results = db.find_one(
        filter=filter_json,
        sort=sort_by
    )

    user = User_db
    user.first_name = results['name']['first']
    user.last_name = results['name']['last']
    user.initials = results['initials']
    user.age = results['age']
    return render_template('edit_record.html', user_id=user_id, user=user)


@app.route("/update_record", methods=['POST'])
def update_record():
    data = request.form
    user = User_db
    user_id = data.get('_id')
    print(user_id)
    user.first_name = data.get('first_name')
    user.last_name = data.get('last_name')
    user.initials = data.get('initials')
    user.age = data.get('age')

    db = open_mongodb_connection()

    filter_json = {
        "_id": ObjectId(user_id)
    }

    sort_by = [('_id', 1)]

    new_values = {"$set":
        {
            "name": {
                'first': user.first_name,
                'last': user.last_name,
            },
            'initials': user.initials,
            'age': user.age,
        }
    }

    results = db.update_one(
        filter=filter_json,
        update=new_values,
        # upsert=False
        # if upsert=True if no record found - a new one will be created
    )


    return render_template('update_confirmation.html', user=user)


app.run(debug=True)
