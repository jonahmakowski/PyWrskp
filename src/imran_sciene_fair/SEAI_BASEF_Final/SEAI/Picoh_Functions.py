from picoh import picoh
import asyncio
import io
from time import sleep
import time
import random
import os
from random import randint
from time import sleep
import PySimpleGUI as sg
from PIL import Image
from Solution_Functions import *
import threading
from threading import Event
#from PySand import *

def forever_funct(stopEvent):
    picoh.reset()
    picoh.setEyeShape("Eyeball")
    picoh_action_functions = [blink_funct, left_wink_funct, right_wink_funct, head_movement, eye_turn, eye_tilt, base_color]
    
    while True:
        if stopEvent.is_set():
            break;
        for func in picoh_action_functions:
            if stopEvent.is_set():
                break;
            func()
            sleep(random.randint(1, 4))
        random.shuffle(picoh_action_functions)
        picoh.setEyeShape("Eyeball")
        #print(picoh_action_functions)

def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(x, y)

async def PicohAcknowledgeNo():
    picoh.setEyeShape("Sad")
    await asyncio.sleep(0.01)
    picoh.say("Alright. I understand", untilDone=False)
    await asyncio.sleep(0.01)
    picoh.setBaseColour(random.randrange(0,10),random.randrange(0,10),random.randrange(0,10))

async def emotion_handler(emotionName, player,emotion_func_message, user):
    await emotion_func_message()
    await asyncio.sleep(0.01)
    EmotionSolutions(emotionName, player, user)

async def Neutral_Handler(emotionName, player, user):
     await emotion_handler(emotionName, player, Neutral_funct_message, user)

async def Fear_Handler(emotionName, player, user):
    await emotion_handler(emotionName, player, fear_funct_message, user)

async def Sadness_Handler(emotionName, player, user):
    await emotion_handler(emotionName, player, sadness_func_message, user)

async def Happiness_Handler(emotionName, player, user):
    await emotion_handler(emotionName, player, happy_func_message, user)

async def Disgust_Handler(emotionName, player, user):
    await emotion_handler(emotionName, player, disgust_func_message, user)

async def  Suprise_Handler(emotionName, player, user):
    await emotion_handler(emotionName, player, Suprise_funct_message, user)

async def Anger_Handler(emotionName, player, user):
    await emotion_handler(emotionName, player, anger_func_message, user)
        

    
def talk_funct():
    picoh.setVoice('-vDavid')
    print (picoh.getDirectory())
    picoh.wait(1)
    picoh.untilDone= picoh.say("Welcome to S-E-A-I: Social, Emotional, Artificial Intelligence.", False,True)
    #await asyncio.sleep(1)
    picoh.wait(4)
    picoh.untilDone= picoh.say("Before we can begin today's session, give me a second to boot", False,True)
    #await asyncio.sleep(1)
    picoh.wait(2)
    picoh.untilDone= picoh.say("I'm ready to help you out today.", False,True)
    #await asyncio.sleep(1)
    picoh.wait(2)

def blink_funct():
    picoh.move(picoh.LIDBLINK, 0)
    sleep(0.2)
    picoh.move(picoh.LIDBLINK, 10)
    random.uniform(0.1,0.4)

def eye_turn():
    picoh.move(picoh.EYETURN, 5)
    sleep(0.2)
    picoh.move(picoh.EYETURN, -5)
    sleep(0.1)
    random.uniform(0.9,5)

def eye_tilt():
    picoh.move(picoh.EYETILT, 5)
    sleep(0.2)
    picoh.move(picoh.EYETILT, -5)
    random.uniform(0.9,5)

def eye_brightness():
    picoh.setEyeBrightness(5)
    sleep(0.1)
    picoh.setEyeBrightness(7)
    sleep(0.5)
    picoh.setEyeBrightness(1)
    sleep(0.5)
    random.uniform(1,6)

def base_color():
    picoh.setBaseColour(10,0,0)
    picoh.wait(randint(1,5))
    picoh.setBaseColour(random.randrange(0,10),random.randrange(0,10),random.randrange(0,10))
    #sleep(1.5)
    #picoh.setBaseColour(random() * 10, random() * 10, random() * 10)
    #picoh.wait(randint(10, 20))
    

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



async def Emotion_Funct(eye_shape, emotion_msg):
    picoh.setBaseColour(0,1,10)
    picoh.setEyeShape(eye_shape)
    await asyncio.sleep(0.01)
    picoh.say(emotion_msg, untilDone=False)
    await asyncio.sleep(0.01)

async def Happy_funct():
    await Emotion_Funct("Heart", 
                  "Whenever you're happy, I'm happy!")

async def happy_func_message(): 
    picoh.say("Party on dude!!", untilDone=True)
    await asyncio.sleep(0.01)
    picoh.playSound('smash',untilDone = True)
    await asyncio.sleep(0.01)
    picoh.setEyeBrightness(10)
    #Satisfying()
    
async def Anger_funct():
    await Emotion_Funct("Sad", 
                  "I see you are angry. I'm sorry for what has happen. If you want, I can help you out. I'll load up a window and you can press either the yes or no to get my advice.")
        
async def anger_func_message():
    picoh.setEyeBrightness(5)
    picoh.say("Alright. I understand. You want help. That makes sense. So, give me a second and I'll set up the system.",untilDone = False)
    picoh.playSound('spring',untilDone = True)
       
async def Disgust_funct():
    await Emotion_Funct("Sad", 
                  "Are you ok my friend? If you are feeling sick, press yes immediatly!")
    
async def disgust_func_message(): 
    picoh.setEyeBrightness(5)
    picoh.say("Alright. I understand. You want help. That makes sense. So, give me a second and I'll set up the system.", untilDone=True)

async def Fear_funct():
    await Emotion_Funct("Sad", 
                  "You're afraid? I'm so sorry. Please, let me know if I can help")
async def fear_funct_message():
    picoh.setEyeBrightness(5)
    picoh.say("Alright, scaredy cat. I only jest. Let me help you out. Just give me a second.", untilDone=True)

async def Sadness_funct():
    await Emotion_Funct("Sad", 
                  "I see you are saddened. What happened??. If you want, I can help you out. I'll load up a window and you can press either the yes or no to get my advice.")

async def sadness_func_message(): 
    picoh.setEyeBrightness(5)
    picoh.say("Alright. Sad Sack. I understand. You want help. That makes sense. So, give me a second and I'll set up the system.", untilDone=True )


async def Surprise_funct():
    await Emotion_Funct("SunGlasses", 
                  "I see you are surprised. Are you alright?? If you want, I can help you out. I'll load up a window and you can press either the yes or no to get my advice.")

async def Suprise_funct_message():
    picoh.setEyeBrightness(5)
    picoh.playSound('spring',untilDone = False)
    picoh.say("Ah. I understand. Something frigthened you. Let me see if I can help you.", untilDone=True)

async def neutral_funct():
    await Emotion_Funct("Glasses", 
                  "I see you are neutral. Are you alright?? I want to make sure if you are feeling neutral or I'm not noticing. Regardless, I can help you out. I'll load up a window and you can press either the yes or no to get my advice.")
async def Neutral_funct_message():
    picoh.setEyeBrightness(5)
    picoh.say("Alright I get it. You need some help. I understand. You aren't feeling Neutral. That suprises me. But regardless, I'll help out ", untilDone=True)
"""
def picoh_yap():
    # Default synthesizer SAPI.  Default Voice as set in Control Panel
    picoh.say("I.  I just took a ride")
    # Quieter
    picoh.setVoice("-a82")
    picoh.say("In a silver machine.")
    # Faster
    picoh.setVoice("-r4")
    picoh.say("And I'm still feeling mean.")
    # Slower
    picoh.setVoice("-r-4")
    picoh.say("Do you wanna ride? See yourself going by.")
    # American
    picoh.setVoice("-vzira")
    picoh.say("The other side of the sky.")
    # Default voice
    picoh.setVoice("")
    picoh.say("I got a silver machine.")

async def emotion_window(hWnd, window_name, emotion_func_message, solution_func):
        sg.theme("DarkBlue")
        await asyncio.sleep(0.01)
        cwd = os.getcwd()
        fname = cwd +  '\\image_file.gif'
        img = Image.open(fname)
        await asyncio.sleep(0.01)
        bio = io.BytesIO()
        await asyncio.sleep(0.01)
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
                await asyncio.sleep(0.01)
                await emotion_func_message()
                window.Close()
                solution_func(hWnd)
            elif event == 'No':
                window.Close()
                picoh.say("Alright. I understand", untilDone=False)
        window.Close()
"""