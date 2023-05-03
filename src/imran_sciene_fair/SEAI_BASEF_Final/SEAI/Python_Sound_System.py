#from re import L
import io
#from getkey import getkey, keys
import PySimpleGUI as sg
import asyncio
import threading
import picoh
import tkinter
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
import pygame

cwd = os.getcwd()
fname = cwd +  '\\image_file.jpg'

img = Image.open(fname)
bio = io.BytesIO()
img.save(bio, format="GIF")

def main():
     sg.theme("DarkBlue")

     layout = [[sg.Image(data=bio.getvalue(), key='key1', size=(428, 240))],
              [sg.Button('Play'), sg.Button('Close'),sg.Exit()],
              [sg.Text("Relaxation Sounds",size=(40,20), justification="center", font="Helvetica 20")]

              ]
     window = sg.Window('Play_Sound',layout,size=(480, 400),finalize=True)         
              
     while True:
      event, values = window.Read()
      if event in (None, 'Exit'):
        break
      if event == 'Play':
        pygame.mixer.init()
        pygame.mixer.music.load("Resources/RelaxingMusic.mp3")
        pygame.mixer.music.play()  
      elif event == 'Close':
        window.Close()        
        picoh.untilDone=picoh.say("Alright. I understand")
   
main()