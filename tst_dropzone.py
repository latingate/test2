import os

from flask import Flask, render_template, request, session
from flask_dropzone import Dropzone
from datetime import datetime
from random import random
from mp3_id3_tags_eyed import MP3tags
from gs_functions import none2empty
import json

mp3tags = MP3tags()
mp3tags.file = "song.mp3"
mp3tags.image_front_cover = 'song2.jpg'
mp3tags.title = 'song name'
mp3tags.artist = 'gal sarig'
mp3tags.genre = 'Pop'
mp3tags.set_tags()

# https://flask-dropzone.readthedocs.io/en/latest/configuration.html

# basedir = os.path.abspath(os.path.dirname(__file__))
basedir = os.getcwd()
upload_path = os.path.join(basedir, 'uploads')
app = Flask(__name__)
app.secret_key = 'caliy!DCB8927d%^ruscvfhjcnv374ytfu' + str(int(random() * 10000))
# session.clear()

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
    # print('session_mp3:', session['mp3'])
    if request.method == 'POST':
        f = request.files.get('files')
        print(f.filename)
        print(datetime.now().strftime("%y%m%d%H%M%S") + '_' + str(int(random() * 10000)))
        file_extension = os.path.splitext(f.filename)[1][1:].lower()
        if file_extension == 'mp3':
            session['mp3'] = f.filename
            print("This is mp3 file: ", session['mp3'])
        image_file_extensions = ('jpg', 'jpeg', 'png')
        if (file_extension in image_file_extensions):
            session['image'] = f.filename
            print("This is image file")
        f.save(os.path.join(upload_path, f.filename))
        if session['mp3']:
            x = MP3tags()
            x.file = os.path.join(upload_path, session['mp3'])
            # session['tags_from_file'] = json.dumps((x.get_tags().__dict__))
            session['tags_from_file'] = (x.get_tags().__dict__)
            # print(session['tags_from_file']['title'])
    return render_template('tst_dropzone.html')


@app.route("/mp3edit_save", methods=['POST'])
def mp3edit_save():
    error = {}
    session['error'] = ['0']
    session['error_message'] = ['no error']
    if 'tags_from_file' in session:
        tags = session['tags_from_file']
    else:
        tags = {}
    if "mp3" not in session:
        mp3_file = ''
        session['error'].append(1)
        session['error_message'].append('No mp3 file found')
        error[1] = 'no mp3'
    else:
        mp3_file = session['mp3']
    data = request.form
    title = data.get('title')
    artist = data.get('artist')
    # print('song name:', title, 'artist', artist, 'erorr codes', session['error'], 'error messages', session['error_message'], 'error dictioanry', error)

    header_data = ('', 'נתון נוכחי בקובץ ה-mp3', 'נתון חדש')

    rows_data = (
        ('שם השיר', none2empty(tags['title']), title),
        ('שם האומן', none2empty(tags['artist']), artist),
        ('מלחין', none2empty(tags['composer'])),
        ('שם האומן של האלבום', none2empty(tags['album_artist'])),
        ('קובץ mp3', '', mp3_file),
        # ('שגיאות','',error)
    )

    table_classes = 'table-striped table-bordered table-hover'
    header_classes = 'text-center bg-secondary bg-opacity-50'
    row_classes = ''
    cell_classes = 'align-self-start'

    col_classes = {
        # 3: 'text-start'
        # text-start / text-end / text-center
    }
    session.clear()
    return render_template('tst_dropzone_results.html', title=title, artist=artist, mp3_file=mp3_file,
                           tags=tags,
                           error=error,
                           header_data=header_data, rows_data=rows_data, table_classes=table_classes,
                           header_classes=header_classes, row_classes=row_classes, cell_classes=cell_classes,
                           col_classes=col_classes
                           )
    # return render_template('update_confirmation.html', user='ok')


if __name__ == '__main__':
    app.run(debug=True)
