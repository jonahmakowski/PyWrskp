from ast import Try
import io
from msilib import Win64
import os
import datetime
import numpy as np
import PySimpleGUI as sg
import cv2
import feat
from feat import Detector
from pathlib import Path
import asyncio
import threading
from tkinter.ttk import *
import keyboard
import os
import threading
from threading import Thread
import time
import random
from random import randint
from time import sleep
from PIL import Image
from picoh import picoh
from PySand import *


emotionThreadDone = True
   
 
async def forever_funct():
    while True:
        blink_funct()
        await asyncio.sleep(5)

        left_wink_funct()
        await asyncio.sleep(5)

        right_wink_funct()
        await asyncio.sleep(5)

        head_movement()
        await asyncio.sleep(5)


def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(x, y)

def emotion_window(window_name, emotion_func_message):
        sg.theme("DarkBlue")
        cwd = os.getcwd()
        fname = cwd +  '\\image_file.gif'
        img = Image.open(fname)
        bio = io.BytesIO()
        img.save(bio, format="GIF")
        layout = [[sg.Image(data=bio.getvalue(), key='key1', size=(428, 240))],
                  [sg.Button('Yes'), sg.Button('No'), sg.Exit()],
                  [sg.Text("Do You Need Some Help", size=(40,20), justification="center", font="Helvetica 20")]
                  ]                
        window = sg.Window(window_name,layout,size=(480, 400),finalize=True)

        while True:        
            event, values = window.Read()
            if event in (None, 'Exit'):
             break
            if event == 'Yes':
             emotion_func_message()
             window.Close()
            elif event == 'No':
             window.Close()
             picoh.untilDone=picoh.say("Alright. I understand")
        window.Close()
def Neutral_window():
     emotion_window('Neutral_Window', Neutral_funct_message)
def Fear_window():
    emotion_window('Fear_Window', fear_funct_message)

def sadness_window():
        emotion_window('Sadness_Window', sadness_func_message)

def happiness_window():
        emotion_window('Happiness_Window', happy_func_message)

def disgust_window():
        emotion_window('Disgust_Window', disgust_func_message)

def  Suprise_window():
    emotion_window('Fear_Window', Suprise_funct_message)

def anger_window():
    emotion_window('Anger_Window', anger_func_message)
        

    
async def talk_funct():
    picoh.untilDone= picoh.say("Welcome to S-E-A-I: Social, Emotional, Artificial Intellegence.", False,True)
    await asyncio.sleep(5)
    picoh.wait(2)
    picoh.untilDone= picoh.say("Before we can begin today's session, give me a second to boot", False,True)
    await asyncio.sleep(6)
    picoh.wait(2)
    picoh.untilDone= picoh.say("I'm ready to help you out today. But first, as always, I need to explain how to turn me off but still have the program run. You just need to press the escape key and I'll shut down.", False,True)
    picoh.wait(5)
    picoh.untilDone = picoh.say("One last thing. I want you to know that the session will start when you press the spacebar ")
    await asyncio.sleep(5)
    picoh.wait(2)


def blink_funct():
    picoh.move(picoh.LIDBLINK, 0)
    sleep(0.2)
    picoh.move(picoh.LIDBLINK, 10)
    random.uniform(0.1,0.4)
    

def left_wink_funct():
    for x in range(10,0,-1):
        picoh.move(picoh.LIDBLINK,x,eye = 1)
        random.uniform(2,2.5)
        

    for x in range(0,10):
        picoh.move(picoh.LIDBLINK,x,eye = 1)
        random.uniform(2,2.5)
        

def right_wink_funct():
    for x in range(10,0,-1):
        picoh.move(picoh.LIDBLINK,x,eye = 2)
        random.uniform(2,2.5)
        

    for x in range(0,10):
        picoh.move(picoh.LIDBLINK,x,eye = 2)
        random.uniform(2,2.5)
       
def head_movement():
    picoh.move(picoh.EYETURN,random.uniform(3.2,7.2),1)
    picoh.move(picoh.EYETILT,random.uniform(3.2,7.2),1)
    sleep(0.5)
    picoh.move(picoh.HEADTURN,random.uniform(3.2,7.2),1)
    picoh.move(picoh.HEADNOD,random.uniform(3.2,7.2),1)
    sleep(0.5)
    picoh.move(picoh.EYETURN,random.uniform(5.2,5.2),1)
    picoh.move(picoh.EYETILT,random.uniform(5.2,5.2),1)
    random.uniform(0.0,2.0)

def Emotion_Funct(eye_shape, emotion_msg, window_func):
    picoh.setBaseColour(0,1,10)
    picoh.setEyeShape(eye_shape)
    picoh.untilDone=picoh.say(emotion_msg)
    window_func()

def Happy_funct():
    Emotion_Funct("Heart", 
                  "Whenever you're happy, I'm happy!",
                  happiness_window)

def happy_func_message(): 
    picoh.untilDone=picoh.say("Party on dude!!")
    Satisfying()
    
def Anger_funct():
        picoh.setBaseColour(0,1,10)
        picoh.setEyeShape("Sad")
        picoh.untilDone= picoh.say("I see you are angered. I'm sorry for what has happen. If you want, I can help you out. I'll load up a window and you can press either the yes or no to get my advice.")
        anger_window()
        
def anger_func_message():
    picoh.untilDone=picoh.say("Alright. I understand. You want help. That makes sense. So, give me a second and I'll set up the system.")
    
       
def Disgust_funct():
    Emotion_Funct("Sad", 
                  "Are you ok my friend? If you are feeling sick, press yes immediatly!",
                  disgust_window)
    
def disgust_func_message(): 
    picoh.untilDone=picoh.say("Alright. I understand. You want help. That makes sense. So, give me a second and I'll set up the system.")

def Fear_funct():
    Emotion_Funct("Sad", 
                  "You're afraid? I'm so sorry. Please, let me know if I can help",
                  Fear_window)
def fear_funct_message():
    picoh.untillDone = picoh.say("Alright, scaredy cat. I only jest. Let me help you out. Just give me a second.")
def Sadness_funct():
    Emotion_Funct("Sad", 
                  "I see you are saddened. What happened??. If you want, I can help you out. I'll load up a window and you can press either the yes or no to get my advice.",
                  sadness_window)

def sadness_func_message(): 
    picoh.untilDone=picoh.say("Alright. Sad Sack. I understand. You want help. That makes sense. So, give me a second and I'll set up the system.")


def Surprise_funct():
    Emotion_Funct("Heart", 
                  "I see you are surpised. Are you alright?? If you want, I can help you out. I'll load up a window and you can press either the yes or no to get my advice.",
                  Suprise_window)

def Suprise_funct_message():
    picoh.untillDone= picoh.say("Ah. I understand. Something frigthened you. Let me see if I can help you.")

def neutral_funct():
    Emotion_Funct("Sad", 
                  "I see you are neutral. Are you alright?? I want to make sure if you are feeling neutral or I'm not noticing you want, I can help you out. I'll load up a window and you can press either the yes or no to get my advice.",
                  Neutral_window)
def Neutral_funct_message():
    picoh.untillDone = picoh.say("Alright I get it. You need some help. I understand. You aren't feeling Neutral. That suprises me.But regardless, I'll help out ")


def ESCKey():
    picoh.close()
    
    


async def key_usage():
    keyboard.add_hotkey("h",Happy_funct)
    keyboard.add_hotkey("a",Anger_funct)
    keyboard.add_hotkey("s",Sadness_funct)
    keyboard.add_hotkey("d",Disgust_funct)
    keyboard.add_hotkey("esc",ESCKey)
    #keyboard.add_hotkey("s",s_key)
    await asyncio.sleep(0)

async def forever_talk():
    talk_funct()
    await asyncio.sleep(0)

#async def picoh_movement():
        #keyboard.add_hotkey("b", blink_funct)
        #keyboard.add_hotkey("l",left_wink_funct)
        #keyboard.add_hotkey("r",right_wink_funct)
        #await asyncio.sleep(0)

async def call_tests():
    await asyncio.gather(key_usage(),forever_funct(), talk_funct())

async def main():
    emotion_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']

    downloads_path = os.path.join(Path.home(), "Downloads\\pyFeatData\\" + datetime.datetime.now().strftime('%Y%m%d %H%M%S'))
    #initialize the emotion detector
    detector = Detector(
        face_model="retinaface",
        landmark_model="mobilefacenet",
        au_model='xgb',
        emotion_model="resmasknet",
        facepose_model="img2pose",
    )

 
    # define the window layout New Window with Emotion Text Holer, Video and Exit Button
    layout = [[sg.Text("Emotion Detection Demo", size=(40, 1), justification="center", font="Helvetica 20")],
              [sg.Image(filename="", key="srcImg")],
              [sg.Text("Detected Emotion", justification="center", font="Helvetica 14", key="detectedEmotion")]
              ]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - Emotion Detection',layout, location=(800, 400))
    # Start Video Capture
    cap = cv2.VideoCapture(0,  cv2.CAP_DSHOW)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(downloads_path + '\\output.avi', fourcc, 24.0, (640, 480))

    os.mkdir(downloads_path)
    sg.theme("DarkBlue")


    savedMaxIndex = 6
    numRepeat = 0

    picoh.reset()

    #detector
    # Capture frames and detect emotion. Exit if "Exit" button is clicked
    while True:
        event, values = window.read(timeout=20)

        if event == sg.WIN_CLOSED:
            break

        ret, frame = cap.read()
        out.write(frame)
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window["srcImg"].update(data=imgbytes)

        try:
            detected_faces = detector.detect_faces(frame)
            detected_landmarks = detector.detect_landmarks(frame, detected_faces)
            #detected_aus = detector.detect_aus(frame, detected_landmarks)
            detected_emotions = detector.detect_emotions(frame, detected_faces, detected_landmarks)
            emVals = detected_emotions[0]
            max_emotion_index = np.argmax(emVals[0]) 
            if(savedMaxIndex == max_emotion_index):
                numRepeat = numRepeat + 5
            else:
                numRepeat = 0
                savedMaxIndex = max_emotion_index

            window["detectedEmotion"].Update(emotion_labels[max_emotion_index])
            if(numRepeat >=3):
                    if savedMaxIndex==0:
                        Anger_funct()
                    elif savedMaxIndex==1:
                        Disgust_funct()
                    elif savedMaxIndex==2:
                        Fear_funct()
                    elif savedMaxIndex==3:
                        Happy_funct()
                    elif savedMaxIndex==4:
                        Sadness_funct()
                    elif savedMaxIndex==5:
                        Surprise_funct()
                    elif savedMaxIndex==6:
                        neutral_funct()

        except Exception as e:
            print(e)
            pass

#        if(emotionThreadDone):
#            emotionThreadDone = False
            #logEmotion = threading.Thread(target=showImageAndEmotion)
            #logEmotion.start()

        # Another way to exit`
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
    # Release camera
    cap.release()
    out.release()
    cv2.destroyAllWindows()

async def picoh_alive():
    await asyncio.gather(main(), forever_funct())

#asyncio.run(call_tests())
asyncio.run(picoh_alive())

#tasks = [forever_talk(),picoh_movement, keys_usage ]
#await asyncio.gather(*tasks)

    #threads = [
    #Thread(target = self.picoh_movement),
    #Thread(target = self.keys_usage),
    #Thread(target = self.forever_talk)
    #]
#for thread in thread:
    #thread.start()

#for thread in thread:
    #thread.join()

