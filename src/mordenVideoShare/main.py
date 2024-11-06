from fileinput import filename
from flask import *
import os
app = Flask(__name__)

ALLOWED_EXTENSIONS = ['mp4']

NAME = 'Morden Video Share'


@app.route('/', methods=['GET', 'POST'])
def home():
    with open('video_locations.txt') as file:
        file_locations = file.readlines()
    processed_locations = []
    for location in file_locations:
        temp = location.split('|')
        author = temp[2].split('.')[0]
        location = 'video/{}'.format(location)
        processed_locations.append({'title': temp[0], 'description': temp[1], 'author': author, 'location': location})

    return render_template('home.html', name=NAME, videos=processed_locations)


@app.route('/upload/<error>', methods=['POST', 'GET'])
def upload(error):
    match error:
        case 'none':
            error = ''
        case 'notmp4':
            error = 'The provided file is not in the MP4 Format'
        case 'unexpected':
            error = 'An unexpected error has occurred, please try again'
    return render_template("upload.html", error=error, title=NAME+' | Posting')


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
    author = 'temp'
    f = request.files['file']
    if allowed_file(f.filename):
        safe_filename = safe_file(f.filename)
        f.save(safe_filename)
        end_filename = '{}|{}|{}.{}'.format(title,
                                            description,
                                            author,
                                            safe_filename.rsplit('.', 1)[1].lower())
        os.rename(os.path.abspath(os.getcwd())+'/'+safe_filename,
                  os.path.abspath(os.getcwd())+'/templates/video/'+end_filename)
        with open('video_locations.txt', 'w') as file:
            file.writelines([end_filename])
        return render_template("upload_success.html",
                               name=f.filename,
                               text=title,
                               title=NAME+' | Upload Successful')
    else:
        return redirect('/upload/notmp4')


if __name__ == '__main__':
    app.run(port=1000, host="0.0.0.0")
