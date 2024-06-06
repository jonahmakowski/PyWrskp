import subprocess
import PySimpleGUI as sg
import os
import ollama


def run_app(app):
    subprocess.run(['bash', 'actions.sh', 'app', f"{app}"])


def open_file(file, loc=None):
    if loc is not None:
        subprocess.run(['bash', 'actions.sh', '-l', loc, 'open', f"{file}"])
    else:
        subprocess.run(['bash', 'actions.sh', 'open', f"{file}"])


def open_web(url):
    subprocess.run(['bash', 'actions.sh', 'web', f"{url}"])


def python_run(file, loc=None):
    if loc is not None:
        subprocess.run(['bash', 'actions.sh', '-l', loc, 'python', f"{file}"])
    else:
        subprocess.run(['bash', 'actions.sh', 'python', f"{file}"])


def start_music():
    subprocess.run(['bash', 'actions.sh', 'play'])


def create_file(file):
    subprocess.run(['bash', 'actions.sh', 'create', f"{file}"])


def stop_music():
    subprocess.run(['bash', 'actions.sh', 'pause'])


def ask_ai(prompt):
    respones = ollama.chat(model='llama3', messages=
               [{'role': 'system', 'content': "You are an ai assistant running locally on the user's computer"},
                {'role': 'user', 'content': prompt}])
    layout = [[sg.Text('LLAMA3 Said:')],
              [sg.Text(respones['message']['content'])],
              [sg.Button('OK', bind_return_key=True)]]
    w = sg.Window('Your AI response', layout.copy())
    w.Read()
    w.close()
    return


def remove_keyword(text, keyword):
    text_lis = text.split()
    text_lis.remove(keyword)
    return ' '.join(text_lis)


def place_in_top_right(window):
    screen_width = window.TKroot.winfo_screenwidth()
    x = screen_width - window.size[0]
    y = 0
    window.TKroot.geometry(f'+{x}+{y}')
    return window


def parse_command(command):
    match command:
        case "Open App":
            app = sg.popup_get_text('What app do you want to open?')
            run_app(app)
        case "Open File":
            file = sg.popup_get_file('', no_window=True)
            open_file(file)
        case "Open Website":
            open_web(remove_keyword(command, 'web'))
        case "Run Python":
            file = sg.popup_get_file('', no_window=True)
            python_run(file)
        case "Play Music":
            start_music()
        case "Create File":
            layout = [[sg.Text('Select folder:'), sg.Input(key='-IN-'), sg.Button('Browse')],
                      [sg.Text('File Name:'), sg.Input(key='-FILE-')],
                      [sg.Button('Go'), sg.Button('Exit')]]

            window = sg.Window('File Browse Example', layout.copy())

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    return

                if event == 'Browse':
                    file_chosen = sg.popup_get_folder('', no_window=True)
                    if file_chosen:
                        window['-IN-'].update(file_chosen + '/')

                if event == 'Go':
                    file = window['-FILE-'].get()
                    folder = window['-IN-'].get()
                    break
            window.close()
            create_file(folder + file)
        case "Pause Music":
            stop_music()
        case "Ask AI":
            prompt = sg.popup_get_text('What do you want to ask AI?')
            ask_ai(prompt)


def run_assistant():
    layout = [[sg.Text('Choose a command', expand_x=True, justification='center')],
              [sg.Combo(['Choose a Command', 'Open App', 'Open File', 'Open Website', 'Run Python', 'Play Music',
                         'Create File', 'Pause Music', 'Ask AI'], default_value='Choose a Command')],
              [sg.Button('Ok', bind_return_key=True), sg.Button('Terminate'), sg.Button('Place in top right')]]
    window = sg.Window('Your Assistant', layout, keep_on_top=True)

    window.read(timeout=0)
    place_in_top_right(window)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Terminate':
            break

        if event == "Place in top right":
            window = place_in_top_right(window)
        else:
            parse_command(values[0])


if __name__ == "__main__":
    run_assistant()
