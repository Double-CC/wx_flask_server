import os
from flask import Flask, request, send_from_directory
from werkzeug import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['PHOTO_FOLDER_B'] = 'photo/body'
app.config['PHOTO_FOLDER_C'] = 'photo/clothes'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':

        # get the data from wx
        code = request.form['code']
        name = request.values.get('name')

        print(name)
        print(code)
        # get openid from wx server
        # url = ""
        # r = requests.get(url)

    return name


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/bodypicture', methods=['GET', 'POST'])
def upload_body():
    print(request)
    if request.method == 'POST':
        file = request.files['file']
        user = request.form['user']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            p = os.path.join(app.config['UPLOAD_FOLDER'], app.config['PHOTO_FOLDER_B'], filename)
            file.save(p)
        # save the id and path to the database



@app.route('/clothespicture', methods=['GET', 'POST'])
def upload_clothes():
    print(request)
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            p = os.path.join(app.config['UPLOAD_FOLDER'], app.config['PHOTO_FOLDER_C'], filename)
            file.save(p)
        # save the id and path to the database


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)