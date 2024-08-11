import subprocess
import PySimpleGUI as sg
import os
import ollama
import speech_recognition as sr
import playsound
from gtts import gTTS
import threading
import time
from fuzzywuzzy import process

is_speaking = False


def find_closest_command(user_input, command_list):
    closest_match, score = process.extractOne(user_input, command_list)
    return closest_match, score


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        playsound.playsound("speak-sound.mp3")
        audio_text = r.listen(source)
        playsound.playsound("speak-sound.mp3")

        try:
            text = r.recognize_google(audio_text)
        except:
            speak_text("Unfortunately I didn't catch that. Please try again")
            text = None

    if text is not None: print('User said: ' + text)
    return text


def speak_text(text, wait=True):
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    def play_audio():
        global is_speaking
        is_speaking = True
        playsound.playsound("speech.mp3")
        is_speaking = False
        os.remove("speech.mp3")
    thread = threading.Thread(target=play_audio)
    thread.start()

    if wait:
        while is_speaking:
            time.sleep(0.1)


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


def ai_backend(chat):
    responses = ollama.chat(model='llama3', messages=chat)
    chat.append(responses['message'])
    return responses['message']['content'], chat


def ask_ai():  # doesn't use action.sh because it doesn't play well with python
    layout = [
        [sg.Text('Chatbot', expand_x=True, justification='center', font=('Helvetica', 20))],
        [sg.InputText(key='-INPUT-')],
        [sg.Button('Send', bind_return_key=True), sg.Button('Goodbye')],
        [sg.Multiline(key='-CHAT-HISTORY-', size=(40, 10), disabled=True)],
    ]

    window = sg.Window('AI Chat', layout.copy())

    chat_history = ''
    chat_history_raw = [{'role': 'system', 'content': "You are an ai assistant running locally on the user's computer"}]

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Goodbye":
            window.close()
            break
        elif event == 'Send':
            user_input = values['-INPUT-']
            chat_history_raw.append({'role': 'user', 'content': user_input})
            response, chat_history_raw = ai_backend(chat_history_raw)  # Replace with your own function
            chat_history += f'User: {user_input}\n'
            chat_history += f'Chatbot: {response}\n'
            window['-CHAT-HISTORY-'].update(chat_history)
            window['-INPUT-'].update('')


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
    lower_command = command.lower()
    if "open app" in lower_command:
        app = remove_keyword(command, 'open')
        app = remove_keyword(app, 'app').title()
        run_app(app)
        speak_text("Opened {}".format(app))
    elif "open file" in lower_command:
        file = sg.popup_get_file('', no_window=True)
        open_file(file)
        speak_text("Opened File")
    elif "search" in lower_command:
        keyword = remove_keyword(command, 'search')
        if keyword == '':
            speak_text('What would you like to search?')
            keyword = listen()
            if keyword is None:
                return
        speak_text("Searching the web for {}".format(keyword), wait=False)
        open_web("duckduckgo.com/?hps=1&q="+keyword)
    elif "run python" in lower_command:
        file = sg.popup_get_file('', no_window=True)
        speak_text("Running the python file", wait=False)
        python_run(file)
    elif "play music" in lower_command:
        speak_text("Playing music")
        start_music()
    elif "create file" in lower_command:
        layout = [[sg.Text('Select folder:'), sg.Input(key='-IN-'), sg.Button('Browse')],
                  [sg.Text('File Name:'), sg.Input(key='-FILE-')],
                  [sg.Button('Go'), sg.Button('Exit')]]

        window = sg.Window('Create File', layout.copy())

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
        speak_text("File Created!")
    elif "pause music" in lower_command:
        stop_music()
        speak_text("Pausing Music")
    elif "ai chat" in lower_command:
        ask_ai()
        speak_text("Opening your AI assistant!")
    elif "ai" in lower_command or "intelligence" in lower_command:
        keyword = "ai" if "ai" in lower_command else "intelligence"
        message = remove_keyword(lower_command, keyword)
        if message == '':
            speak_text('What would you like to ask AI?')
            message = listen()
            if message is None:
                return
        speak_text("Asking AI {}".format(message), wait=False)
        response, chat = ai_backend([{'role': 'system', 'content': "You are an ai assistant running locally on the user's computer. Respond in short sentances unless instructed otherwise"},
                                     {'role': 'user', 'content': message}])
        speak_text(response)
    elif "what time is it" in lower_command:
        speak_text("It's currently {}.".format(time.strftime("%I:%M %p", time.localtime())))
    elif "show commands" in lower_command or "help" in lower_command:
        speak_text("Here is a list of commands you can use", wait=False)
        sg.popup("open app\t-\tOpens an app as specified\n"
                 "open file\t-\tOpens a file as specified\n"
                 "search\t-\tSearches something in Duckduckgo\n"
                 "run python\t-\tRuns a python file as provided by the opened file explorer\n"
                 "play music\t-\tPlays music in spotify\n"
                 "pause music\t-\tPauses music in spotify\n"
                 "create file\t-\tCreates a file as specified\n"
                 "ai\t-\tOpens an ai chat window", title="Help Window")
    else:
        speak_text('This is an invalid command', wait=False)
        command, score = find_closest_command(command, ['open file',
                                                        'search',
                                                        'run python',
                                                        'play music',
                                                        'pause music',
                                                        'create file',
                                                        'intelligence',
                                                        'ai',
                                                        'what time is it'])
        while is_speaking:
            time.sleep(0.1)

        speak_text('Did you mean to say {}?'.format(command))

        while True:
            response = listen()
            if 'yes' in response:
                parse_command(command)
                break
            elif response is not None:
                speak_text('Ok, please try again')
                break


def run_assistant():
    layout = [[sg.Button('Terminate'), sg.Button('Listen')]]
    window = sg.Window('Your Assistant', layout, keep_on_top=True)

    window.read(timeout=0)
    place_in_top_right(window)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Terminate':
            break
        else:
            text = listen()
            if text is None:
                continue
            parse_command(text)


if __name__ == "__main__":
    run_assistant()
