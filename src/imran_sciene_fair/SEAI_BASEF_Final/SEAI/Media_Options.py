global dst_path
global file2
global emotion
def notify():
    username = "Picoh"
    message = 'Guess what?? Its all complete!'
    font1, font2 = ("Arial", 20, 'bold'), ('Courier New', 16, 'italic')
    test = sg.popup_notify("{}:\n{}".format(username, message), title='A message from Picoh')

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

def emotion_selection_media(suffix):
    print("Incomplete")
    #This function will be used to copy the file from the location it was placed to the nessacary emotion folder
    try:
            if emotion == "happy":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Happy " + suffix)
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "sad":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Sad " + suffix)
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "neutral":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Neutral " + suffix)
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            elif emotion == "surprise":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\Surprise " + suffix)
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "anger":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\ Anger " + suffix)
                            import shutil
                            shutil.move(dst_path,final_path)
                            import os
                            try:
                                os.replace(file2, final_path)
                                print("Complete")
                            except:
                                notify()
            if emotion == "fear":
                            final_path = ("C:\\Users\\Imran Allarakhia\\source\\repos\\PQT5S\\PQT5S\\ Fear " + suffix)
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

def emotion_selection_sound(suffix):
    emotion_selection_media("Videos")

def emotion_selection_video(suffix):
    emotion_selection_media("Sounds")


def media_window():
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
    layout = [
             [sg.Text("Main Video", size=(40, 1), justification="center", font="Helvetica 20")],
              [sg.Image(filename='', key='image')],
              [sg.Button("Options")],
              [sg.Button("Start Screen")],
              [sg.Cancel("Exit")],
              ]
    # create the window and show it without the plot
    window = sg.Window('Demo Application - Emotion Detection',layout, location=(800, 400),finalize=True)

    while True:
        event, values = window.read(timeout=20)

        if event == sg.WIN_CLOSED:
            break
        if event == 'Options':
            start = sg.popup("Options Include Vidoes Sounds and Themes,", image="Resources\\picoh_animated.gif")
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
                        emotion_selection_sound()
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
