from flask import Flask
from flask import render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/converter', methods=['GET', 'POST'])
def converter_page():
    if request.method == 'GET':
        return render_template('converter.html')

@app.route('/converter/base_convert', methods=['POST']) 
def base_convert():
    base10 = int(request.form['base10'])
    return render_template('converter.html', base10_result="{:x}".format(base10).upper())

@app.route('/converter/hexa_convert', methods=['POST'])
def hexa_convert():
    hexadecimal = request.form['hexadecimal']
    return render_template('converter.html', hexadecimal_result=str(int(hexadecimal, 16)))

if __name__ == '__main__':
    app.run()
