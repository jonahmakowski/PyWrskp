import subprocess
import PySimpleGUI as sg
import os
import ollama

def run_app(app):
    """
    Executes a bash script with the provided application name as an argument.

    Args:
        app (str): The name of the application to be passed to the bash script.

    Returns:
        None
    """
    subprocess.run(['bash', 'actions.sh', 'app', f"{app}"])

def open_file(file, loc=None):
    """
    Opens a file using a bash script.

    Parameters:
    file (str): The name or path of the file to open.
    loc (str, optional): An optional location parameter to be passed to the bash script. Defaults to None.

    Returns:
    None
    """
    if loc is not None:
        subprocess.run(['bash', 'actions.sh', '-l', loc, 'open', f"{file}"])
    else:
        subprocess.run(['bash', 'actions.sh', 'open', f"{file}"])

def open_web(url):
    """
    Opens a web page using a bash script.

    Args:
        url (str): The URL of the web page to open.

    Returns:
        None
    """
    subprocess.run(['bash', 'actions.sh', 'web', f"{url}"])

def python_run(file, loc=None):
    """
    Executes a Python script using a bash script.

    Parameters:
    file (str): The path to the Python file to be executed.
    loc (str, optional): An optional location argument to be passed to the bash script.

    If 'loc' is provided, the command executed will be:
    'bash actions.sh -l <loc> python <file>'
    
    If 'loc' is not provided, the command executed will be:
    'bash actions.sh python <file>'
    """
    if loc is not None:
        subprocess.run(['bash', 'actions.sh', '-l', loc, 'python', f"{file}"])
    else:
        subprocess.run(['bash', 'actions.sh', 'python', f"{file}"])

def start_music():
    """
    Starts playing music by running a bash script.

    This function uses the subprocess module to run a bash script named 'actions.sh'
    with the argument 'play'. The script is expected to handle the logic for playing music.

    Raises:
        subprocess.CalledProcessError: If the subprocess call fails.
    """
    subprocess.run(['bash', 'actions.sh', 'play'])

def create_file(file):
    """
    Creates a file by running a bash script.

    Args:
        file (str): The name of the file to be created.
    """
    subprocess.run(['bash', 'actions.sh', 'create', f"{file}"])

def stop_music():
    """
    Stops the music by running a shell script.

    This function executes a bash script named 'actions.sh' with the 'pause' argument
    to stop the currently playing music.

    Note:
        Ensure that 'actions.sh' is located in the same directory as this script
        and has the necessary permissions to be executed.

    Raises:
        subprocess.CalledProcessError: If the subprocess call fails.
    """
    subprocess.run(['bash', 'actions.sh', 'pause'])


def ai_backend(chat):
    """
    Processes a chat conversation using the Ollama AI model and returns the latest response.

    Args:
        chat (list): A list of dictionaries representing the chat history. Each dictionary should have a 'message' key.

    Returns:
        tuple: A tuple containing the latest response content (str) and the updated chat history (list).
    """
    responses = ollama.chat(model='llama3', messages=chat)
    chat.append(responses['message'])
    return responses['message']['content'], chat


def ask_ai():  # doesn't use action.sh because it doesn't play well with python
    """
    Launches a simple AI chat interface using PySimpleGUI.

    The function creates a window with a text input for user messages, a send button, 
    a goodbye button, and a multiline text area to display the chat history. 
    It maintains a chat history and interacts with an AI backend to generate responses.

    The chat history is updated with each user input and AI response. The window 
    closes when the user clicks the 'Goodbye' button or closes the window.

    Note:
        The function `ai_backend` should be defined elsewhere to handle the AI response 
        generation based on the chat history.

    Layout:
        - A centered title 'Chatbot' with a large font.
        - An input text field for user messages.
        - A 'Send' button (binds to the return key) and a 'Goodbye' button.
        - A multiline text area to display the chat history (disabled for editing).

    Events:
        - 'Send': Sends the user input to the AI backend and updates the chat history.
        - 'Goodbye' or window close: Closes the chat window.

    Returns:
        None
    """
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
    """
    Removes the first occurrence of a specified keyword from a given text.

    Args:
        text (str): The input text from which the keyword will be removed.
        keyword (str): The keyword to be removed from the text.

    Returns:
        str: The text with the first occurrence of the keyword removed.

    Raises:
        ValueError: If the keyword is not found in the text.
    """
    text_lis = text.split()
    text_lis.remove(keyword)
    return ' '.join(text_lis)


def place_in_top_right(window):
    """
    Places the given window in the top right corner of the screen.

    Args:
        window: An object representing the window to be positioned. 
                It must have the attributes 'TKroot' (the Tkinter root window) 
                and 'size' (a tuple containing the width and height of the window).

    Returns:
        The window object with its position updated to the top right corner of the screen.
    """
    screen_width = window.TKroot.winfo_screenwidth()
    x = screen_width - window.size[0]
    y = 0
    window.TKroot.geometry(f'+{x}+{y}')
    return window

def parse_command(command):
    """
    Parses and executes a given command.

    Parameters:
    command (str): The command to be parsed and executed. Possible values are:
        - "Open App": Prompts the user to enter the name of an app to open and runs it.
        - "Open File": Prompts the user to select a file and opens it.
        - "Open Website": Opens a website specified in the command.
        - "Run Python": Prompts the user to select a Python file and runs it.
        - "Play Music": Starts playing music.
        - "Create File": Prompts the user to select a folder and enter a file name, then creates the file.
        - "Pause Music": Pauses the currently playing music.
        - "Ask AI": Initiates an AI interaction.

    Returns:
    None
    """
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
            ask_ai()


def run_assistant():
    """
    Launches the assistant GUI and handles user interactions.

    The function creates a window with a dropdown menu for selecting commands,
    and buttons for confirming the selection, terminating the application, 
    or placing the window in the top right corner of the screen. It continuously 
    listens for user events and processes them accordingly.

    Commands available in the dropdown menu:
    - 'Choose a Command'
    - 'Open App'
    - 'Open File'
    - 'Open Website'
    - 'Run Python'
    - 'Play Music'
    - 'Create File'
    - 'Pause Music'
    - 'Ask AI'

    Event handling:
    - If the 'Terminate' button or window close button is pressed, the loop breaks and the application terminates.
    - If the 'Place in top right' button is pressed, the window is repositioned to the top right corner.
    - For other commands selected from the dropdown, the `parse_command` function is called with the selected command.

    Note:
    - The function assumes the existence of `place_in_top_right` and `parse_command` functions.
    - The window is initially placed in the top right corner upon creation.

    Returns:
        None
    """
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
