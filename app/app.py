import os
from os.path import join, dirname
from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, patch_request_class

app = Flask(__name__, static_folder='./static')
dropzone = Dropzone(app)

app.config['SECRET_KEY'] = 'supersecretkeygoeshere'
EXTS = 'aiff aif aifc afc wav mp3 mp4 m4a'

# Flask-Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = False
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
#app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = False
# https://flask-dropzone.readthedocs.io/en/latest/configuration.html#file-type-filter
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = ', '.join(['.'+ext for ext in  EXTS.split()])
#app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'
# ALLOW up to 5 GB
app.config['DROPZONE_MAX_FILE_SIZE'] = 5000 # 5 GB
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Flask-Uploads settings
app.config['UPLOADS_DEFAULT_DEST'] = join(dirname(__file__), 'uploads')
print(app.config['UPLOADS_DEFAULT_DEST'])


photos = UploadSet(name='files', extensions=(EXTS))
configure_uploads(app, photos)
patch_request_class(app, size=5000*1024*1024*1024)  # Allow up to 5 GiB


@app.route('/', methods=['GET', 'POST'])
def index():
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']
    # handle image upload from Dropszone
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
    return render_template('index.html')


@app.route('/results')
def results():
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))
        
    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)
    # 複数画像には未対応
    for url in file_urls:
        print(file_urls)
        #detected, result = classify.classify(url)
    

    return render_template('results.html', file_urls=file_urls, result=None)

if __name__ == "__main__":
    app.run(port=9999, debug=True)
