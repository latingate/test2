from flask import Flask, redirect, request, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

import os

# Drag & Drop upload
# Source: https://medium.com/@dustindavignon/upload-multiple-images-with-python-flask-and-flask-dropzone-d5b821829b1d

# In flask_uploads.py
# Change:
# from werkzeug import secure_filename,FileStorage
# to:
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

dropzone = Dropzone(app)

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'upload_results'

# Uploads settings
# upload_folder = 'uploads'
# app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + upload_folder
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route("/")
def home():
    s = "This is Gal's server"
    s += "<br/>Other routes:"
    s += "<br/><a href='/gal'>/gal</a>"
    s += "<br/><a href='/test'>/test</a>"
    s += "<br/><a href='/upload'>/upload</a>"
    return s


admin_name = 'Gal Sarig'


@app.route("/gal")
def gal():
    return "This is /gal route"


@app.route("/test")
def template():
    first_name = 'Gal'
    last_name = 'Sarig'
    return render_template('flask_test.html', name=first_name + ' ' + last_name, admin_name=admin_name)


# secret key for session / cookies
app.config['SECRET_KEY'] = 'mcpYc982y3hufjWnv8'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
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


app.run(debug=True)
