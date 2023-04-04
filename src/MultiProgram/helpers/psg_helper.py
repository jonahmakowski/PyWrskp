import PySimpleGUI as psg


def question_window(question, title):
    return psg.popup_get_text(question, title=title)


def notification(text):
    psg.popup_notify(text)


def show_window(text, title):
    psg.popup_ok(text, title=title)


def clear():
    os.system('clear')
    