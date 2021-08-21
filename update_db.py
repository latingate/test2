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
        Initials: {self.initials}
        Age: {self.age}
        Pics: {self.pics}
        ''')

    _id: str
    first_name: str
    last_name: str
    initials: str
    age: int
    pics: dict


@app.route("/ajax_include", methods=['POST', 'GET'])
def ajax_include():
    return render_template('ajax_include.html')


@app.route("/ajax_include_in", methods=['POST'])
def ajax_include_in():
    result = request.form.get('result')
    return render_template('ajax_include_in.html', result=result)
    # return jsonify({'data': render_template('test_in.html', result=result)})


@app.route("/list_records_new", methods=['GET', 'POST'])
def list_records_new():
    cursor = get_records()
    return render_template('list_records.html', cursor=cursor)


@app.route("/", methods=['GET', 'POST'])
@app.route("/list_records", methods=['GET', 'POST'])
def list_records():
    search_string = request.form.get('search_string') if request.form.get('search_string') else ''
    page_size = request.form.get('page_size', default=0)
    # page_size = page_size if page_size else 0
    # if not page_size:
    #     page_size = 0
    page_numnber = request.form.get('page_number', default=1)
    print(page_numnber)
    db = open_mongodb_connection()
    # search_string = ''
    filter_json = {"$or": [
        {
            "name.first": {
                "$regex": f'.*{search_string}.*',  # includes
                "$options": 'i'  # case insensitive
            }
        },
        {
            "name.last": {
                "$regex": f'.*{search_string}.*',  # includes
                "$options": 'i'  # case insensitive
            }
        }
    ],
    }

    sort_by = [('_id', 1)]

    cursor = db.find(
        filter=filter_json,
        sort=sort_by,
        limit=page_size,
        # batch_size=3
        # TODO batch_size is not working
    )

    return render_template('list_records.html', cursor=cursor, filter_json=filter_json, sort_by=sort_by)


@app.route("/get_records", methods=['GET', 'POST'])
def get_records():
    search_string = request.form.get('search_string') if request.form.get('search_string') else ''
    db = open_mongodb_connection()
    # search_string = ''
    filter_json = {"$or": [
        {
            "name.first": {
                "$regex": f'.*{search_string}.*',  # includes
                "$options": 'i'  # case insensitive
            }
        },
        {
            "name.last": {
                "$regex": f'.*{search_string}.*',  # includes
                "$options": 'i'  # case insensitive
            }
        }
    ]
    }

    sort_by = [('_id', 1)]
    cursor = db.find(
        filter=filter_json,
        sort=sort_by,
    )
    results = list(cursor)
    # print(results)
    # return render_template('list_records.html', cursor=cursor, filter_json=filter_json, sort_by=sort_by)
    # return jsonify(cursor=cursor, search_string=search_string)
    return str(results)


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

    new_values = {"$set": {
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


@app.route("/find_user", methods=['POST'])
def find_user():
    # find the first user whose first name includes the search string, letter insensitive
    if request.method == 'GET':
        search_string = request.args.get('search_string')
    if request.method == 'POST':
        search_string = request.form.get('search_string')

    db = open_mongodb_connection()

    filter_json = {
        "name.first": {
            "$regex": f'.*{search_string}.*',  # includes
            "$options": 'i'  # case insensitive
        }
    }

    sort_by = [('_id', 1)]

    results = db.find_one(
        filter=filter_json,
        sort=sort_by
    )

    s = results

    user = User()
    # user._id = ObjectId(results['_id'])
    user.first_name = s['name']['first']
    user.last_name = s['name']['last']
    user.initials = s['initials']
    user.age = s['age']
    user.pics = {}

    return jsonify(user_id=str(s['_id']), user=user.__dict__, query_filter=filter_json)


@app.route("/add_db_user")
def add_db_user():
    conn = MongoClient('mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
    db_main = conn['tstdb']
    user = 'tst1'
    password = '12345'
    db_main.add_user(user, password, roles=[{
        'role': 'root',
        'db': 'admin',
    }])
    return f"db user '{user}' created"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

# ajax - result-->
# $(#div).html = render(get_results)
# ajax render template flask
