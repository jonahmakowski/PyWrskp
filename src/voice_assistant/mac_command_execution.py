import os
from webbrowser import open as web_open
from urllib.parse import quote


def open_app(app):
    os.system("open /Applications/{}.app".format(app))


def open_directory_in_files(directory):
    os.system("open {}".format(directory))


def open_file(file):
    os.system("open {}".format(file))


def open_webpage(page):
    web_open(page)


def google_search(search):
    base_url = "https://www.google.com/search?q="
    final_url = base_url + quote(search)
    open_webpage(final_url)
