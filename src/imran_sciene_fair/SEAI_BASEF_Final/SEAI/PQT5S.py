import PySimpleGUI as sg
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
global dst_path
global file2
global emotion

def create_folder_funct():
    print("Incomplete for now")
    import os
    if not os.path.exists('Happy Vidoes'):
        os.makedirs('Happy Videos', exist_ok=True)   

    if not os.path.exists('Happy Sounds'):
        os.makedirs('Happy Sounds', exist_ok=True)   
   
    if not os.path.exists('Sad Sounds'):
        os.makedirs('Sad Sounds', exist_ok=True)

    if not os.path.exists('Sad Videos'):
        os.makedirs('Sad Vidoes', exist_ok=True)
    
    if not os.path.exists('Suprise Sounds'):
        os.makedirs('Suprise Sounds', exist_ok=True)

    if not os.path.exists('Suprise Videos'):
        os.makedirs('Suprise Videos', exist_ok=True)
    
    if not os.path.exists('Neutral Sounds'):
        os.makedirs('Neutral Sounds', exist_ok=True)

    if not os.path.exists('Neutral Videos'):
        os.makedirs('Neutral Videos', exist_ok=True)


    if not os.path.exists('Anger Sounds'):
        os.makedirs('Anger Sounds', exist_ok=True)

    if not os.path.exists('Anger Videos'):
        os.makedirs('Anger Videos', exist_ok=True)

    if not os.path.exists('Disgust Sounds'):
        os.makedirs('Disgust Sounds', exist_ok=True)

    if not os.path.exists('Disgust Videos'):
        os.makedirs('Disgust Videos', exist_ok=True)

    if not os.path.exists('Fear Sounds'):
        os.makedirs('Fear Sounds', exist_ok=True)

    if not os.path.exists('Fear Videos'):
        os.makedirs('Fear Videos', exist_ok=True)

def emotion_selection_sound():
    print("Incomplete")
    #This function will be used to copy the file from the location it was placed to the nessacary emotion folder
    try:
            if emotion == "happy":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Happy Sounds")
                            import shutil
                            shutil.copy(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "sad":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Sad Sounds")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "neutral":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Neutral Sounds")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            elif emotion == "surprise":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Surprise Sounds")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "anger":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\ Anger Sounds")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "fear":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\ Fear Sounds")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
    except:
        print("That is not possible")



    

    
    
   


    #This funct will be used in order to create all the folders nessacary to store all the videos  
def emotion_selection_video():
    print("Incomplete")
    #This function will be used to copy the file from the location it was placed to the nessacary emotion folder
    try:
            if emotion == "happy":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Happy Videos")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "sad":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Sad Videos")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "neutral":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Neutral Videos")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            elif emotion == "surprise":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Surprise Videos")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "anger":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\ Anger Videos")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "fear":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\ Fear Videos")
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
    except:
        print("That is not possible")

    #This function will be used to copy the file from the location it was placed to the nessacary emotion folder

username = ''
password = ''
#PROGRESS BAR
def progress_bar():
    global selected_theme
    global themes 
    themes = sg.ListOfLookAndFeelValues()
    selected_theme = sg.theme('Reds')
    current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
    sg.ChangeLookAndFeel(selected_theme)
    layout = [[sg.Text('Creating your account...')],
            [sg.ProgressBar(200, orientation='h', size=(20, 20), key='progbar')],
            [sg.Cancel()]]

    window = sg.Window('Working...', layout)
    for i in range(200):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()
    notify()

def create_account():
    global selected_theme
    global username, password, email
    global current_them
    global themes

    themes = sg.ListOfLookAndFeelValues()
    selected_theme = sg.theme('Reds')
    current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
    sg.ChangeLookAndFeel(selected_theme)
    layout = [[sg.Text("Sign Up", size =(15, 1), font=40, justification='c')],
             [sg.Text("E-mail", size =(15, 1),font=16), sg.InputText(key='-email-', font=16)],
             [sg.Text("Re-enter E-mail", size =(15, 1), font=16), sg.InputText(key='-remail-', font=16)],
             [sg.Text("Create Username", size =(15, 1), font=16), sg.InputText(key='-username-', font=16)],
             [sg.Text("Create Password", size =(15, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
             [sg.Button("Submit"), sg.Button("Cancel")]]

    window = sg.Window("Sign Up", layout)

    while True:
        event,values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Submit":
                password = values['-password-']
                username = values['-username-']
                if values['-email-'] != values['-remail-']:
                    sg.popup_error("Error: Emails dont match", font=16)
                    continue
                elif values['-email-'] == values['-remail-']:
                    email = values['-email-']
                    progress_bar()
                    break
    window.close()
#create_account()


def login():
    global selected_theme
    global username,password, themes
    global current_them
    global themes

    themes = sg.ListOfLookAndFeelValues()
    selected_theme = sg.theme("Reds")
    current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
    sg.ChangeLookAndFeel(selected_theme)
    layout = [[sg.Text("Log In", size =(15, 1), font=40)],
            [sg.Text("Username", size =(15, 1), font=16),sg.InputText(key='-usrnm-', font=16)],
            [sg.Text("Password", size =(15, 1), font=16),sg.InputText(key='-pwd-', password_char='*', font=16)],
            [sg.Button('Ok'),sg.Button('Cancel')]]

    window = sg.Window("Log In", layout)

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "Ok":
                if values['-usrnm-'] == username and values['-pwd-'] == password:
                    sg.popup("Welcome!")
                    print(username)
                    print(password)
                    print(email)
                    send_email()
                    run_funct()
                    notify()
                    break
                elif values['-usrnm-'] != username or values['-pwd-'] != password:
                    sg.popup("Invalid login. Try again")
    window.close

def send_email():
    global selected_theme
    global current_them
    import smtplib
    import ssl
    sender_email = ("1allarakhimr@hdsb.ca")
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    receiver_email = email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Welcome to SEAI!"

    body = "Thank you for signing up to the SEAI system. You will now be able to cutomize your account and this information will be saved and can be reused whenever you so please."
    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()

    if receiver_email == "":
          login() 
    else:
            password = "ytym"
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                #server.ehlo()  # Can be omitted
                server.starttls(context=context)
                #server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
    sg.popup("You have been sent an email")

def run_funct():
    new_window()

async def new_window():
    print("This Worked")
    import sys
    import PySimpleGUI as sg
    import cv2 
    from PIL import Image
    import io
    import numpy as np
    from textwrap import wrap 
    from sys import exit as exit
    global selected_theme
    global current_them
    global themes
    themes = sg.ListOfLookAndFeelValues()
    selected_theme = sg.theme = "Reds"
    current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
    sg.ChangeLookAndFeel(selected_theme)
    menudef = ['Notes',['Developer Notes','User Notes']],['Manual',['User Manual','Developer Manual']],['FAQs',['Developer FAQs','User FAQs']]
    layout = [[sg.Menu(menudef)],
        [sg.Text("Main Video", size=(40, 1), justification="center", font="Helvetica 20")],
               [sg.Image(filename='', key='image')],
              [sg.Button("Options")],
              [sg.Button("Start Screen")],
              [sg.Cancel("Exit")],
              ]
    # create the window and show it without the plot
    window = sg.Window('Demo Application - Emotion Detection',layout, location=(800, 400),finalize=True)
    cap = cv2.VideoCapture(0,  cv2.CAP_DSHOW)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
    while True:
        ret, frame = cap.read()
        imgbytes = cv2.imencode('.png', frame)[1].tobytes()  # ditto
        window['image'].update(data=imgbytes)
    #detector
    # Capture frames and detect emotion. Exit if "Exit" button is clicked
        event, values = window.read(timeout=20)

        if event == sg.WIN_CLOSED:
            break
        if event == 'Start Screen':
            start_window()
        if event == 'Options':
            start = sg.popup("Options Include Vidoes Sounds and Themes,", image="C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\picoh-orange-buy_1.png")
            answer = sg.popup_get_text("Do you want to change the theme, add sounds, add vidoes, or add website", title = "What do you want to change?")
            if answer == 'website':
                print('Okay')
                text = sg.popup_get_text("Enter in the name of website")
                link = sg.popup_get_text("Enter in the link to the website")
                check = sg.popup_yes_no("Are you satisfied with your choice")
                if check == "Yes":
                    print("Okay")
                    print(text,link,check)
                    import webbrowser
                    webbrowser.open(link)
                    notify()
                 
            if answer == 'sound':
                print('okay2')
                file2=sg.popup_get_file('Select a file',  title="File selector")
                print ("File selected", file2)
                src_path = sg.popup_get_file('Select the folder the file is in', title="Old Folder")
                dst_path=sg.popup_get_folder('Get folder', title="Folder selector")
                print ("Folder selected",dst_path)
                ch = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                emotion2 = sg.popup_notify("Your choices are happy,sad,anger,fear,neutral, sadness, surpise, and disgust ")
                emotion = sg.popup_get_text("Enter in which emotion you want this video to register as")
                try:
                    if emotion == "happy":
                         ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                         if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                         if ch2 == "no":
                            print("Okay I understand") 

                    if emotion == "sad":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             emotion_selection_video()
                             print("Okay. You are sure about it so I'll do as you say")
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "suprise":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             emotion_selection_video()
                             print("Okay. You are sure about it so I'll do as you say")
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "neutral":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "anger":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "disgust":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "fear":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                        if ch2 == "no":
                            print("Okay I understand")
                            
                except:
                    sg.popup_notify("That is not an option.Sorry.")
                ch = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                if ch == "Yes":
                        print("Okay. Now. I'll move the file to that location. Please make sure that the file was placed in a folder inside of where you store the code for best optimization ")
                        import shutil
                        shutil.move(src_path,dst_path)
                        emotion_selection_sound
                        import os
                        try:
                            os.replace(file2, dst_path)
                            emotion_selection_sound()
                        except:
                            print("Complete")
                            emotion_selection_sound
                if ch == "no":
                    print("Okay I understand")
                notify()
                print(ch,src_path,dst_path,file2)
                

            if answer == 'theme':
                    print('okay3')
                    theme_choice = sg.popup("Choose a theme from the options above: ")
                    themes = sg.ListOfLookAndFeelValues()
                    selected_theme = 'Reds'
                    current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
                    sg.ChangeLookAndFeel(selected_theme)

                    layout = [
                            [sg.T('User Setting:')],
                            [sg.Text('Select Theme:'), 
                            sg.Combo(values=themes, default_value=selected_theme, size=(15, 1), enable_events=True, key='select_theme')],
                            [sg.I('this is input')], 
                            [sg.B('Hello'), sg.Button(' about ', key='about')]
                    ]

                    window = sg.Window('', layout=layout)

                    while True:
                        e, v= window()
                        if e is None:
                            break
       
                        elif e == 'select_theme':
        
                                selected_theme = v['select_theme']
                                print(selected_theme)
                                current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]

                                try:
                                    window_bkg = current_them.get('BACKGROUND')
                                    window.TKroot.config(background=window_bkg)
                                except Exception as e:
                                        print(e)

                                 # iterate over all widgets:
                                for v, element in window.AllKeysDict.items():
                                # for child in window.TKroot.frame.children.values():
                
                                    try:
                                        color = current_them.get(element.Type.upper())
                                        if color:
                                            if element.Type == 'button':
                                                element.Widget.config(foreground=color[0], background=color[1])
                                            else:
                                                element.Widget.config(background=color)

                                            element.update()
                                            notify()
                                    except Exception as e:
                                        print(e)
            if answer == 'video':
                print('okay4')
                theme_choice = sg.popup("Choose a theme from the options above: ")
                themes = sg.ListOfLookAndFeelValues()
                selected_theme = 'Reds'
                current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
                sg.ChangeLookAndFeel(selected_theme)
                file2=sg.popup_get_file('Select a file',  title="File selector")
                print ("File selected", file2)
                src_path = sg.popup_get_file('Select the folder the file is in', title="Old Folder")
                dst_path=sg.popup_get_folder('Get folder', title="Folder selector")
                print ("Folder selected",dst_path)
                emotion2 = sg.popup_notify("Your choices are happy,sad,anger,fear,neutral, sadness, surpise, and disgust ")
                emotion = sg.popup_get_text("Enter in which emotion you want this video to register as")
                try:
                    if emotion == "happy":
                         ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                         if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                         if ch2 == "no":
                            print("Okay I understand") 

                    if emotion == "sad":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             emotion_selection_video()
                             print("Okay. You are sure about it so I'll do as you say")
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "suprise":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             emotion_selection_video()
                             print("Okay. You are sure about it so I'll do as you say")
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "neutral":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "anger":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "disgust":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                        if ch2 == "no":
                            print("Okay I understand")

                    if emotion == "fear":
                        ch2 = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                        if ch2 == "Yes":
                             print("Okay. You are sure about it so I'll do as you say")
                             emotion_selection_video()
                        if ch2 == "no":
                            print("Okay I understand")
                            
                except:
                    sg.popup_notify("That is not an option.Sorry.")
                ch = sg.popup_yes_no("Do you want to Continue?",  title="YesNo")
                if ch == "Yes":
                        print("Okay. Now. I'll move the file to that location. Please make sure that the file was placed in a folder inside of where you store the code for best optimization ")
                        import shutil
                        shutil.move(src_path,dst_path)
                        import os
                        try:
                            os.replace(file2, dst_path)
                        except:
                            notify()
                if ch == "no":
                    print("Okay I understand") 
                    print(ch,src_path,dst_path,file2)
                    #video_conveter()

#Make this window with popups to store videos and video locations and access them

async def developer_note_window():
    print("This worked")
#Create a New Window to show all of the devloper notes with diagrams
async def user_notes():
    print("This worked")
#Create a New Window to show the user notes with images
async def developer_manual():
    print("This Worked")
#Create a manual with popups to help developers understand the smaller details of the code 
async def user_manual():
    print("This worked")
#Create a manual with popups to help users understand the system
async def developer_faq():
    print("This Worked")
#Create a window where when you press buttons for certain questions, it opens a popup window with the answer and the same applies with the other faq window
async def user_faq():
    print("This Worked")
#Create a window where when you press buttons for certain questions, it opens a popup window with the answer and the same applies with the other faq window

def start_window():
    import PySimpleGUI as sg
    global selected_theme
    global current_them
    global themes
    themes = sg.ListOfLookAndFeelValues()
    selected_theme = sg.theme("Reds")
    current_them = sg.LOOK_AND_FEEL_TABLE[selected_theme]
    sg.ChangeLookAndFeel(selected_theme)
    menudef = ['Notes',['Developer Notes','User Notes']],['Manual',['User Manual','Developer Manual']],['FAQs',['Developer FAQs','User FAQs']]
    layout = [[sg.Menu(menudef)],
             [sg.Text('SEAI Start Up', size=(40,20),font=40,justification = 'c')],
              [sg.Button('Login'),sg.Button('Create Account')],
               [sg.Cancel()],
              ]
    window = sg.Window('SEAI Start Up', layout)  
    while True:
        event,values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        if event == 'Login':
            login()
        if event == 'Developer Notes':
            asyncio.run(developer_note_window())
        if event == 'User Notes':
            asyncio.run(user_notes())
        if event =='Create Account':
            create_account()
    window.close()
def notify():
    username = "Picoh"
    message = 'Guess what?? Its all complete!'
    font1, font2 = ("Arial", 20, 'bold'), ('Courier New', 16, 'italic')
    test = sg.popup_notify("{}:\n{}".format(username, message), title='A message from Picoh')
import asyncio
create_folder_funct()
(start_window())
