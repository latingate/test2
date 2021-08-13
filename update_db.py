from flask import Flask, redirect, request, render_template, request, session, url_for, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from dataclasses import dataclass
import json
import os

from gs_functions import *

app = Flask(__name__)


@dataclass(init=False)
class User:
    def display(self):
        print(f'''
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Initlas: {self.initials}
        Age: {self.age}
        Pics: {self.pics}
        ''')

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

    user = User()
    user.first_name = results['name']['first']
    user.last_name = results['name']['last']
    user.initials = results['initials']
    user.age = results['age']
    # user.pics= {}
    # user.display()
    return render_template('edit_record.html', user_id=user_id, user=user)


@app.route("/update_record", methods=['POST'])
def update_record():
    data = request.form
    user = User
    user_id = data.get('_id')
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


@app.route("/get_user_id", methods=['POST'])
def get_user_id():
    db = open_mongodb_connection()

    if request.method == 'GET':
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')

    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

    filter_json = {
        "name.first": first_name,
        "name.last": last_name
    }

    sort_by = [('_id', 1)]

    results = db.find_one(
        filter=filter_json,
        sort=sort_by
    )

    user = User()
    # user._id = ObjectId(results['_id'])
    user.first_name = results['name']['first']
    user.last_name = results['name']['last']
    user.initials = results['initials']
    user.age = results['age']
    user.pics = {}
    print(user.__dict__)

    return jsonify(user_id=str(results['_id']), user=user.__dict__, query_filter=request.form)
    # return jsonify(user_id=str(results['_id']), raw_results=str(results), error=0, message="success")
    # return str(results['_id'])
    # return user.__dict__


app.run(debug=True, port=5000)
