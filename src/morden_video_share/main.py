from distutils.log import debug 
from fileinput import filename 
from flask import *
import os
app = Flask(__name__) 

ALLOWED_EXTENSIONS = ['mp4', 'jpeg', 'jpg', 'mov', 'png', 'gif']

@app.route('/') 
def main():
    return render_template("upload.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def safe_file(filename):
    

@app.route('/success', methods = ['POST', 'GET']) 
def success():
    text = request.form['text']
    try:
        f = request.files['file']
        if text == '':
            text = f.filename
        if allowed_file(f.filename):
            f.save(f.filename)
            os.rename(f.filename, text)
            return render_template("upload_success.html", name=f.filename, text=text)
        else:
            return redirect('/')
    except:
        return redirect('/')

if __name__ == '__main__': 
    app.run()
