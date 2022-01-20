from flask import Flask, redirect, request, render_template, request, session, url_for, jsonify

from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from pymongo import MongoClient
import json
import os

from mp3_id3_tags_eyed import edit_mp3
from gs_functions import *

# Drag & Drop upload
# Source: https://medium.com/@dustindavignon/upload-multiple-images-with-python-flask-and-flask-dropzone-d5b821829b1d
#
# In flask_uploads.py
# Change:
# from werkzeug import secure_filename, FileStorage
# to:
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage


app = Flask(__name__)

dropzone = Dropzone(app)

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*, .pdf'
# app.config['DROPZONE_REDIRECT_VIEW'] = 'upload_results'

# Uploads settings
upload_folder = 'uploads'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/' + upload_folder
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route("/")
def home():
    return render_template('home.html')


admin_name = 'Gal Sarig'


@app.route("/gal")
def gal():
    return "This is /gal route"


@app.route("/test")
def test():
    first_name = 'Gal'
    last_name = 'Sarig'
    return render_template('flask_test.html', name=first_name + ' ' + last_name, admin_name=admin_name)


@app.route("/test2/<name1>")
def test2(name1):
    first_name = 'Gal'
    last_name = 'Sarig'
    return render_template('flask_test.html', name=first_name + ' ' + last_name, admin_name=admin_name, name1=name1)


# secret key for session / cookies
app.config['SECRET_KEY'] = 'mcpYc982y3hufjWnv8'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    app.config['DROPZONE_REDIRECT_VIEW'] = 'upload_results'
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropzone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)

            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename
            )
            # append image urls
            file_urls.append(photos.url(filename))

        session['file_urls'] = file_urls
        i = 0
        file_urls_dic = {"pic" + str(++i): url for url in file_urls}
        print(file_urls_dic)
        return "uploading..."
    # return dropzone template on GET request
    return render_template('upload.html')


@app.route('/upload_results')
def upload_results():
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('upload'))

    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)

    return render_template('upload_results.html', file_urls=file_urls)


@app.route("/jquery")
def jquery():
    return render_template('jquery.html')


@app.route('/_add_numbers', methods=['POST', 'GET'])
def _add_numbers():
    if request.method == 'GET':
        a = request.args.get('a')
        b = request.args.get('b')
        total = int(a) + int(b)
        # another way:
        # a = request.args.get('a', 0, int)
        # b = request.args.get('b', 0, int)
        # total = a + b

    if request.method == 'POST':
        a = request.form.get('a')
        b = request.form.get('b')
        total = int(a) + int(b)

    return jsonify(result=total)


@app.route("/mongodb/<name>")
def mongodb_getone(name):
    db = open_mongodb_connection()

    filter_json = {
        "name.first": name
    }

    sort_by = [('name.first', 1)]

    results = db.find(
        filter=filter_json,
        sort=sort_by
    )

    results_list = list(results)
    results_count = results.count()
    first_record_json = str(results_list[0])
    first_record_dump = json.dumps(first_record_json)
    # name = first_record_dictionary["name"]
    # print(name)
    print('json: ' + first_record_json)
    print('dump / dictionary ?? : ' + first_record_dump)
    return render_template("mongodb_results.html", results_cursor=results, results_list=results_list,
                           first_record_json=first_record_json, results_count=results_count)


@app.route("/table")
def display_table():
    header_data = ('name (english)', 'name (hebrew)', 'age')

    rows_data = (
        ('Gal Sarig', 'גל שריג', 54),
        ('Sigal Lifshitz', 'סיגל ליפשיץ', 49),
        ('Michal Sarig', 'מיכל שריג', 20),
        ('Zohar Gofen', 'זהר גופן', 26)
    )

    table_classes = 'table-striped table-bordered table-hover'
    header_classes = ' text-center'
    row_classes = ''
    cell_classes = ''

    col_classes = {
        1: 'text-start',
        2: 'text-end',
        3: 'text-center'
    }
    return render_template('table.html', header_data=header_data, rows_data=rows_data, table_classes=table_classes,
                           header_classes=header_classes, row_classes=row_classes, cell_classes=cell_classes,
                           col_classes=col_classes)


# Site Map
def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/site_map")
def site_map():
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    return jsonify(links)


@app.route("/mp3edit")
def mp3edit():
    # Dropzone settings
    app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
    app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
    app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*, audio/*'
    # app.config['DROPZONE_REDIRECT_VIEW'] = 'mp3edit_uploads'

    # Uploads settings
    upload_folder = 'uploads'
    app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/' + upload_folder
    photos = UploadSet('photos', IMAGES)
    configure_uploads(app, photos)
    patch_request_class(app)  # set maximum file size, default is 16MB

    return render_template("mp3edit.html")
    # return edit_mp3()

@app.route("/mp3edit_save")
def mp3edit_save():
    return "/mp3edit_save"


@app.route("/mp3edit_uploads")
def mp3edit_uploads():
    return "/mp3edit_uploads"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
