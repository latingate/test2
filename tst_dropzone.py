import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

# https://flask-dropzone.readthedocs.io/en/latest/configuration.html

# basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.getcwd()
app = Flask(__name__)
app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
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
        print(f)
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('tst_dropzone.html')


if __name__ == '__main__':
    app.run(debug=True)
