import PySimpleGUI as psg
import json


def popup(question, title):
    return psg.popup_get_text(question, title=title)


def notification(text):
    psg.popup_notify(text)


def show_window(text, title):
    psg.popup_ok(text, title=title)


def read_file(path):
    try:
        with open(path) as json_file:
            info = json.load(json_file)
        return info
    except FileNotFoundError:
        return None


def write_file(path, save):
    with open(path, 'w') as outfile:
        json.dump(save, outfile)
