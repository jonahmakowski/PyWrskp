from fileinput import filename
from flask import *
import os
app = Flask(__name__)

ALLOWED_EXTENSIONS = ['mp4', 'jpeg', 'jpg', 'mov', 'png', 'gif']

NAME = 'Morden Video Share'


@app.route('/', methods=['GET', 'POST'])
def home():
    return redirect('/upload/none')


@app.route('/upload/<error>', methods=['POST', 'GET'])
def upload(error):
    if error == 'none':
        error = ''
    return render_template("upload.html", error=error, title=NAME+'|Posting')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def safe_file(filename):
    filename = filename.split('/')
    return filename[-1]


@app.route('/success', methods=['POST', 'GET'])
def success():
    title = request.form['title']
    description = request.form['description']
    author = ''
    try:
        f = request.files['file']
        if allowed_file(f.filename):
            safe_filename = safe_file(f.filename)
            f.save(safe_filename)
            end_filename = '{}|{}|{}.{}'.format(title,
                                                description,
                                                author,
                                                safe_filename.rsplit('.', 1)[1].lower())
            os.rename(safe_filename, end_filename)
            return render_template("upload_success.html", name=f.filename, text=text)
        else:
            return redirect('/404')
    except:
        return redirect('/')


if __name__ == '__main__':
    app.run(port=1000, host="0.0.0.0")
