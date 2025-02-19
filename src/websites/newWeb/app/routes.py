from flask import render_template
from app import app

pages = [{'name': 'home', 'locations': ['/', '/home', '/main'], 'html': 'home.html'},
         {'name': 'new site info', 'locations': ['/new_site_info'], 'html': 'new_site.html'},
         {'name': 'print web info', 'locations': ['/print_web_info'], 'html': 'info.html'},
         {'name': 'youtube', 'locations': ['/youtube'], 'html': 'youtube.html'}]


@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
@app.route('/main', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='Welcome')


@app.route('/new_site_info', methods=['POST', 'GET'])
def new_site():
    return render_template('new_site.html', title='New Site Info')


@app.route('/print_web_info', methods=['POST', 'GET'])
def print_web_info():
    for item in pages:
        print('Name: {}'.format(item['name']))
        print('Locations:')
        for t in item['locations']:
            print('\t{}'.format(t))
        print('HTML File: {}'.format(item['html']))
        print()
        print()
    return render_template('info.html', title='Pages Info', website=pages)


@app.route('/youtube')
def youtube():
    return render_template('youtube.html', title='Youtube')
