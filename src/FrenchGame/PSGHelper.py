import PySimpleGUI as sg

def popup(question, title):
    return sg.popup_get_text(question, title=title)


def notification(text):
    sg.popup_notify(text)

def show_window(text, title):
    sg.popup_ok(text, title=title)
