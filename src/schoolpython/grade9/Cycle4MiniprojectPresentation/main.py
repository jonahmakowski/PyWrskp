from flask import Flask
from flask import render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/converter')
def converter_page():
    return render_template('converter.html')

@app.route('/converter/base_convert', methods=['POST', 'GET']) 
def base_convert():
    if request.method == 'GET':
        return redirect(url_for('converter_page'))
    else:
        base10 = int(request.form['base10'])
        return render_template('converter.html', base10_result="{:x}".format(base10).upper(), base_base=base10)

@app.route('/converter/hexa_convert', methods=['POST', 'GET'])
def hexa_convert():
    if request.method == 'GET':
        return redirect(url_for('converter_page'))
    else:
        hexadecimal = request.form['hexadecimal']
        return render_template('converter.html', hexadecimal_result=str(int(hexadecimal, 16)), base_hex=hexadecimal)

@app.route('/')
def redirect_home():
    return redirect(url_for('home'))

@app.route('/information')
def home():
    return render_template('home.html')

@app.route('/bibliography')
def bibliography():
    return render_template('bibliography.html')

if __name__ == '__main__':
    app.run()
