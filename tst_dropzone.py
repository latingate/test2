import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from datetime import datetime
from random import random

# https://flask-dropzone.readthedocs.io/en/latest/configuration.html

# basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.getcwd()
upload_path = os.path.join(basedir, 'uploads')
app = Flask(__name__)
app.config.update(
    # DROPZONE_UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_MAX_FILE_SIZE=12,
    DROPZONE_MAX_FILES=2,
    DROPZONE_INPUT_NAME='files',
    # DROPZONE_ALLOWED_FILE_TYPE = 'audio',
    DROPZONE_ALLOWED_FILE_CUSTOM=True,
    DROPZONE_ALLOWED_FILE_TYPE='image/*, .mp3',
    DROPZONE_DEFAULT_MESSAGE='גרור לפה קובץ mp3 וקובץ תמונה (אם יש)',
    DROPZONE_MAX_FILE_EXCEED='לא ניתן להעלות יותר קבצים',
    DROPZONE_INVALID_FILE_TYPE='לא ניתן להעלות קבצים מסוג זה',
    DROPZONE_FILE_TOO_BIG='הקובץ גדול מידי',
    DROPZONE_TIMEOUT=5 * 60 * 1000)

dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('files')
        print(f.filename)
        print(datetime.now().strftime("%y%m%d%H%M%S") + '_' + str(int(random() * 10000)))
        file_split = os.path.splitext(f.filename)
        file_extension = file_split[1][1:].lower()
        print(file_extension)
        if file_extension == 'mp3':
            print("This is mp3 file")
        image_file_extensions = ('jpg', 'jpeg', 'png')
        if (file_extension in image_file_extensions):
            print("This is image file")
        f.save(os.path.join(upload_path, f.filename))
    return render_template('tst_dropzone.html')

@app.route("/mp3edit_save", methods=['POST'])
def mp3edit_save():
    data = request.form
    song_name = data.get('song_name')
    artist = data.get('artist')
    print(song_name, artist)

    f = request.files.get('file')
    # f.save(app.config['UPLOADED_PHOTOS_DEST'], f.filename)
    print(f.filename)
    # f.save(os.path.join('the/path/to/save', f.filename))
    return song_name
    # return render_template('update_confirmation.html', user='ok')


if __name__ == '__main__':
    app.run(debug=True)
