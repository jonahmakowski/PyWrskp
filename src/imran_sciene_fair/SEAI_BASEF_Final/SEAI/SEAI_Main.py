import os
from datetime import datetime
from tkinter import CURRENT
from typing import Dict
import cv2
import asyncio
from time import sleep
from threading import Thread 
from threading import Event
import queue
import json
import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import io
from pathlib import Path
from feat import Detector
from feat.plotting import animate_face
from feat.utils import openface_AU_presence
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import gc
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Picoh_Functions import *
from Media_Options import *
from user_resources import *

seai_users : Dict

# custom thread
class EmotionDetectionThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

class EmotionData(object):
    def __init__(self, emotionName, emotionFunction):
        self.emotionName = emotionName
        self.emotionFunction = emotionFunction

def HideActionRow(window):
        window['helpText'].update(visible=False)
        window['Yes'].update(visible=False)
        window['No'].update(visible=False)

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')

# Function needed because json library cannot serialize dates
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

# JSon Serializer saves Dictionary of Dictionaries
def serialize(user_dict, filename):
    #strDict = {i:j.__dict__ for i,j in user_dict.items()}
    json.dump( user_dict, open(filename,'w'), default=json_serial )

# JSon Serializer converts Dictionary objects back to Person and then returns dictionary of Persons
def deserialize(filename):
    try:
        user_dict = json.load(open(filename))
    except:
        user_dict = {}
        pass
    return user_dict

async def HandleWindowEvents(event: Event, actionQueue: asyncio.Queue , window, player, downloads_path, stopEvent: Event, analyzingEvent: Event, values):
    global current_user
    global seai_users
    global userfile

    if event == sg.WIN_CLOSED:
        stopEvent.set()
    if event == 'play':
        player.play()
    elif event == 'pause':
         player.pause()
    elif event == 'stop':
        player.stop()            
    elif event == 'Developer Notes':
        sg.popup('Under development')
    elif event == 'User Notes':
        sg.popup('Under development')
    elif event == 'Developer Manual':
        sg.popup('Under development')
    elif event == 'User Manual':
        sg.popup('Under development')
    elif event == 'Developer FAQs':
        sg.popup('Under development')
    elif event == 'User FAQs':
        sg.popup('Under development')
    elif event == 'Options':
        generate_table(current_user)
        seai_users[current_user['username']] = current_user
        serialize(seai_users, userfile)
    elif event == 'Yes':
        HideActionRow(window)
        if not actionQueue.empty():
            emotionData = await actionQueue.get()
            await emotionData.emotionFunction(emotionData.emotionName, player, current_user)
    elif event == 'No':
        HideActionRow(window)
        await PicohAcknowledgeNo()
    elif event == 'Analyze Video':
        ResetCheckBoxes(window)
        await AnalyzeVideos(downloads_path, int(values['txtSkipFrames']), analyzingEvent, values)

def CaptureVideoToFile(frameQueue: queue.LifoQueue, downloads_path, saveModeEvent:Event, saveStopEvent:Event, appStopEvent:Event, analyzingEvent: Event):
    # Initialize Video Frame Capture
    cap = cv2.VideoCapture(0,  cv2.CAP_DSHOW)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
    sleep_seconds=1/24
    #Initialize Video Writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = None
    while True:
        try:
            if analyzingEvent.isSet():
                time.sleep(1)
            else:
                ret, frame = cap.read()
                if ret == False or appStopEvent.is_set():
                    if not out is None:
                        out.release()
                    break;
                frameQueue.put(frame)
                if saveModeEvent.is_set():
                    if out is None:
                        filename = downloads_path+'\\output_' + datetime.now().strftime('%H%M%S') + '.avi'
                        out = cv2.VideoWriter(filename, fourcc, 24.0, (640, 480))
                    out.write(frame)
                if saveStopEvent.is_set():
                    saveStopEvent.clear()
                    if not out is None:
                        out.release()
                        out = None
            time.sleep(sleep_seconds)
        except Exception as e:
            print(e)
            pass
    cap.release()
    if not out is None:
        out.release()

async def captureAndSaveFrame(emotionFrame: asyncio.LifoQueue, actionQueue: asyncio.Queue, window, player, downloads_path, stopEvent: Event, analyzingEvent: Event):
    # Initialize Video Frame Capture
    sleep_seconds=1/24

    # Variables used by thread to save output file
    tFrameCapture = None
    evFileSave = Event()
    evFileSaveStop = Event()
    frameQueue = queue.LifoQueue()
    tFrameCapture = Thread(target=CaptureVideoToFile, args=(frameQueue, downloads_path, evFileSave, evFileSaveStop,stopEvent, analyzingEvent))
    tFrameCapture.start()
    fileSaveMode = False
    await asyncio.sleep(0.5)

    # Capture frames and detect emotion. Exit if "Exit" button is clicked
    while True:
        try:
            event, values = window.read(timeout=20)
            await HandleWindowEvents(event, actionQueue, window, player, downloads_path, stopEvent, analyzingEvent, values)
            if event == sg.WIN_CLOSED:
                break
            if stopEvent.is_set():
                evFileSaveStop.set()
            frame = frameQueue.get_nowait()
            while not frameQueue.empty():
                try:
                    frameQueue.get_nowait()
                    frameQueue.task_done()
                except Exception as e:
                    break;
            #Save Frame to Video File
            await asyncio.sleep(0.001)
            if fileSaveMode == False and values['cbSaveVideo'] == True:
                fileSaveMode = True
                evFileSave.set()
                evFileSaveStop.clear()
            elif fileSaveMode == True and values['cbSaveVideo'] == False: 
                fileSaveMode = False
                evFileSave.clear()
                evFileSaveStop.set()

                #out.write(frame)
            await asyncio.sleep(0.001)

            # Keep the latest frame for detect emotion 
            await emotionFrame.put(frame)

            #Show Frame
            await asyncio.sleep(0.001)
            scaled_frame = cv2.resize(frame, (320, 240))
            imgbytes = cv2.imencode(".png", scaled_frame)[1].tobytes()
            window["srcImg"].update(data=imgbytes)
            await asyncio.sleep(sleep_seconds)
        except Exception as e:
            print(e)
            pass
        # Another way to exit`
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
    print("Capture and Save Frame Done")

def getEmotions(detector, frame, stopEvent: Event):
    try:
        if stopEvent.is_set(): return None
        detected_faces = detector.detect_faces(frame)
        if stopEvent.is_set(): return None
        detected_landmarks = detector.detect_landmarks(frame, detected_faces)
        if stopEvent.is_set(): return None
        detected_aus = detector.detect_aus(frame, detected_landmarks)
        if stopEvent.is_set(): return None
        detected_emotions = detector.detect_emotions(frame, detected_faces, detected_landmarks)
        return [detected_emotions, detected_aus,]
    except Exception as e:
        print(e)
def addressEmotions(func, player, stopEvent: Event):    
    try:
        if stopEvent.is_set(): return None
        func(player)
    except Exception as e:
        print(e)

def AnimateFace(prevAus, currentAus, filename):
    # Initialize Video Frame Capture
    try:
        animate_face(start=prevAus, end=currentAus, muscles={'all':  'heatmap'}, save=filename)
    except Exception as e:
        print(e)
        pass

async def detectAndShowEmotion(lifoQueue: asyncio.LifoQueue, actionQueue: asyncio.Queue, window, player, downloadsPath, stopEvent: Event, analyzingEvent: Event):
    #Initialize Lists containing Emotions and Functions responding to Emotions
    global emotion_labels
    emotion_inital_message = [Anger_funct, Disgust_funct, Fear_funct, Happy_funct, Sadness_funct, Surprise_funct, neutral_funct]
    emotion_solutions = [Anger_Handler, Disgust_Handler, Fear_Handler, Happiness_Handler, Sadness_Handler, Suprise_Handler, Neutral_Handler]
    savedMaxIndex = 6
    numRepeat = 0

    #initialize the emotion detector
    detector = Detector(
        face_model="retinaface",
        landmark_model="mobilefacenet",
        au_model='xgb',
        emotion_model="resmasknet",
        facepose_model="img2pose",
    )
    fig_agg = None
    prevAus = None
    prevSavedIndex = 6

    while True:
        try:
            event, values = window.read(timeout=20)
            await asyncio.sleep(0.001)
            await HandleWindowEvents(event, actionQueue, window, player, downloadsPath, stopEvent, analyzingEvent, values)
            if event == sg.WIN_CLOSED:
                break
            if values['cbDetectEmotions'] == True:
                frame = await lifoQueue.get()
                while not lifoQueue.empty():
                    try:
                        lifoQueue.get_nowait()
                        lifoQueue.task_done()
                    except Exception as e:
                        break;
                t = EmotionDetectionThread(target=getEmotions, args=(detector, frame, stopEvent))
                await asyncio.sleep(0.01)
                t.start()
                await asyncio.sleep(0.01)
                while(t.is_alive()):
                    await(asyncio.sleep(.5))
                res = t.join()
                detected_emotions = res[0]
                if detected_emotions != None:
                    emVals = detected_emotions[0]
                    max_emotion_index = np.argmax(emVals[0]) 
                    detected_aus = res[1]

                    if(savedMaxIndex == max_emotion_index):
                        numRepeat = numRepeat + 1
                    else:
                        numRepeat = 0
                        savedMaxIndex = max_emotion_index

                    await(asyncio.sleep(0.01))
                    if fig_agg:
                        delete_figure_agg(fig_agg)
                    fig, ax = plt.subplots()
                    plt.clf()
                    ax.cla()
                    plt.xlabel('Emotion Value')
                    plt.title('Detected Emotions')
                    plt.barh(emotion_labels, emVals[0], align='center', )
                    fig_agg = draw_figure(window['figCanvas'].TKCanvas, fig)
                    window["detectedEmotion"].Update(emotion_labels[max_emotion_index])
                    if numRepeat > 3:
                        if values['cbEmotionAnimation'] == True:
                            if prevAus is None:
                                prevAus = np.zeros(20)
                            filename = 'emotionAnimation\\em_' + emotion_labels[prevSavedIndex] + '_' + emotion_labels[max_emotion_index]+ '_' +  datetime.now().strftime('%Y%m%d %H%M%S') + '.gif'
                            asyncio.create_task(AnimateFace(prevAus,detected_aus[0], filename))
                            del prevAus
                            prevAus = detected_aus[0]
                            prevSavedIndex = max_emotion_index
                        numRepeat = 0
                        if values['cbPicohTalk'] == True:
                            await(asyncio.sleep(0.01))
                            await emotion_inital_message[max_emotion_index]()
                            await asyncio.sleep(0.001)
                            window['cbDetectEmotions'].update(False)
                            window['cbDetectEmotions'].update(False)
                            window['cbPicohTalk'].update(False)
                            window['helpText'].update(visible=True)
                            window['Yes'].update(visible=True)
                            window['No'].update(visible=True)
                            while not actionQueue.empty():
                                try:
                                    actionQueue.get_nowait()
                                    actionQueue.task_done()
                                except Exception as e:
                                    break;
                            await actionQueue.put(EmotionData(emotion_labels[max_emotion_index], emotion_solutions[max_emotion_index]))
                            await asyncio.sleep(0.001)
                    await asyncio.sleep(0.001)
        except Exception as e:
            print(e)
            pass
    print("Detect and Show Done")

def ResetCheckBoxes(window):
    window['cbDetectEmotions'].update(False)
    window['cbSaveVideo'].update(False)
    window['cbPicohTalk'].update(False)

async def SaveVideoFramesAnalysisAsync(downloads_path, frames, imageNum):
    print("Got here" + str(imageNum))
    try:
        detector = Detector(
            face_model="retinaface",
            landmark_model="mobilefacenet",
            au_model='xgb',
            emotion_model="resmasknet",
            facepose_model="img2pose",
            )
        await asyncio.sleep(.01)
        for frame in frames:
            imgPath = downloads_path+"\\frameIn" +  str(imageNum).zfill(5) + ".png"
            cv2.imwrite(imgPath, frame)
            await asyncio.sleep(.01)
            multi_face_prediction = detector.detect_image(imgPath)
            await asyncio.sleep(.01)
            figs = multi_face_prediction.plot_detections(add_titles=True, muscles=True)
            await asyncio.sleep(.01)
            outputPath = downloads_path + "\\frameOut" + str(imageNum).zfill(5) + ".png"
            plt.savefig(outputPath)
            plt.close(figs[0])
            await asyncio.sleep(.01)
            imageNum = imageNum + 1

    except Exception as e:
        print(e)

def GetFrameCount(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    ret = True
    while ret:
        frame_count = frame_count + 1
        ret, frame = cap.read()
    cap.release()
    return frame_count        

def SaveVideoFrameAnalysis(detector, downloads_path, frame, imageNum):
    try:
        imgPath = downloads_path+"\\frameIn" +  str(imageNum).zfill(5) + ".png"
        cv2.imwrite(imgPath, frame)
        multi_face_prediction = detector.detect_image(imgPath)
        figs = multi_face_prediction.plot_detections(add_titles=True, muscles=True)
        outputPath = downloads_path + "\\frameOut" + str(imageNum).zfill(5) + ".png"
        plt.savefig(outputPath)
        plt.close(figs[0])
        del figs
        del multi_face_prediction
        plt.clf()
    except Exception as e:
        print(e)

def AnalyzeVideos(downloads_path,skipFrames, analyzingEvent: Event, values):
    analyzingEvent.set()
    detector = Detector(
        face_model="retinaface",
        landmark_model="mobilefacenet",
        au_model='xgb',
        emotion_model="resmasknet",
        facepose_model="img2pose",
        )
    included_extensions = ['avi']
    file_names = [fn for fn in os.listdir(downloads_path)
                  if any(fn.endswith(ext) for ext in included_extensions)]
    for filename in file_names:
        AnalyzeVideo(detector, downloads_path, filename,skipFrames, values)
    analyzingEvent.clear()

def AnalyzeVideo(detector, downloads_path, filename, skipFrames, values):
    global emotion_labels
    cap = cv2.VideoCapture(downloads_path + '\\' + filename)
    prefix = filename.split('.')[0]
    dirPath = downloads_path + '\\' + prefix
    if os.path.exists(dirPath):
        return;
    os.mkdir(dirPath)
    ret = True
    
    prevAus = np.zeros(20)
    frameNum = 1
    fCount = skipFrames
    prevSavedIndex = 6
    while True:
        try:
            ret, frame = cap.read()
            if ret == False:
                break;
            if fCount > skipFrames:
                fCount = 0
                SaveVideoFrameAnalysis(detector, dirPath, frame, frameNum)
                if values['cbEmotionAnimation'] == True:
                    detected_faces = detector.detect_faces(frame)
                    detected_landmarks = detector.detect_landmarks(frame, detected_faces)
                    detected_aus = detector.detect_aus(frame, detected_landmarks)
                    detected_emotions = detector.detect_emotions(frame, detected_faces, detected_landmarks)
                    emVals = detected_emotions[0]
                    max_emotion_index = np.argmax(emVals[0])
                    animatedFile = dirPath+ '\\em_' + emotion_labels[prevSavedIndex] + '_' + emotion_labels[max_emotion_index]+ '_' +  str(frameNum).zfill(5) + ".gif"
                    AnimateFace(prevAus,detected_aus[0], animatedFile)
                    del prevAus
                    del detected_faces
                    del detected_landmarks
                    del detected_emotions
                    prevAus = detected_aus[0]
                    prevSavedIndex = max_emotion_index
            frameNum = frameNum + 1
            fCount = fCount + 1
            # Another way to exit
            k = cv2.waitKey(30) & 0xff
            if k == 27: # press 'ESC' to quit
                break 
            del frame
            if frameNum % 200 == 0:
                gc.collect()
        except Exception as e:
            print(e)
            pass
    cap.release()

async def AnalyzeVideoAsync(downloads_path):
    video_path = downloads_path + '\\output.avi'
    number_of_frames = GetFrameCount(video_path)
    cap = cv2.VideoCapture(video_path)
    #number_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    num_threads = 10
    frames_per_thread = int(number_of_frames / num_threads) +1
    ret = True
    
    frameNum = 1
    threadFrameNum = 0
    threadNum = 0
    frames = []
    thread_results = []
    while True:
        try:
            ret, frame = cap.read()

            if threadFrameNum >= frames_per_thread or ret == False:
                thread_results.append(asyncio.create_task(SaveVideoFramesAnalysisAsync(downloads_path, frames, frameNum)))
                frames = []
                threadFrameNum = 0
                frameNum = frameNum + frames_per_thread
                threadNum = threadNum+1

            if ret == False:
                break
            frames.append(frame)
            threadFrameNum = threadFrameNum + 1
            # Another way to exit
            k = cv2.waitKey(30) & 0xff
            if k == 27: # press 'ESC' to quit
                break 
        except Exception as e:
            print(e)
            pass

    asyncio.gather(thread_results)

def AnalyzeVideoOld(downloads_path):
    detector = Detector(
        face_model="retinaface",
        landmark_model="mobilefacenet",
        au_model='xgb',
        emotion_model="resmasknet",
        facepose_model="img2pose",
    )
    video_path = downloads_path + '\\output2.avi'
    video_prediction = detector.detect_video(video_path)
    print(video_prediction.shape)
    video_prediction.emotions.plot()
    skip_frames = int(video_prediction.shape[0]/20)
    if skip_frames == 0:
        skip_frames = 1

    for i in range(0, video_prediction.shape[0], skip_frames):
        try:
            video_prediction.loc[i].plot_detections(faceboxes=True, add_titles=True)
        except Exception as e:
            print(e)
            pass

def btn(name, img_file_rel_path=''):  # a PySimpleGUI "User Defined Element" (see docs)
    return sg.Button(key=name, pad=(1, 1), image_filename=img_file_rel_path)

def create_main_window():
    # define the window layout New Window with Emotion Text Holer, Video and Exit Button
    vidCapColumn = [[sg.Text("Social Emotional Artificial Intelligence", size=(40, 1), justification="center", font="Helvetica 16")],
              [sg.Image(filename="", key="srcImg", size=(320, 240))],
              [sg.Checkbox('Save Video', default=False, key='cbSaveVideo'), sg.Checkbox('Detect Emotions', default=False, key='cbDetectEmotions'), sg.Checkbox('Animation', default=False, key='cbEmotionAnimation'), sg.Checkbox('Picoh Talk', default=False, key='cbPicohTalk')],
              [ sg.Text('Skip Frames', key='lblSkipFrames'), sg.InputText('23', key='txtSkipFrames'),],
              [sg.Button("Analyze Video"), sg.Button("Options")]
              ]
    picohOutputColumn = [[sg.Image('Resources\\picoh_animated.gif', key='picoh_image', size=(428, 240))],
                         [sg.Text("Detected Emotion", justification="center", font="Helvetica 14", key="detectedEmotion")],
                         [sg.Text("Do you need some help?", justification="left", font="Helvetica 14", key="helpText", visible=False), sg.Button('Yes', visible=False), sg.Button('No', visible=False)],
                         #[sg.Canvas(size=(480, 270), key='-VID_OUT-')],
                         [sg.Image('',size=(480, 270), key='-VID_OUT-')],
                         [btn('play', 'Resources\\MPAssets\\play_off.png'), btn('pause', 'Resources\\MPAssets\\pause_off.png'), btn('stop','Resources\\MPAssets\\stop.png')]
                        ]
    resultsOutputColumn = [[sg.Canvas(key='figCanvas', size=(480,360))]]
        
    sg.ChangeLookAndFeel("Reds")
    menudef = ['Notes',['Developer Notes','User Notes']],['Manual',['User Manual','Developer Manual']],['FAQs',['Developer FAQs','User FAQs']]
    layout = [
        [sg.Menu(menudef)],
        [sg.Column(vidCapColumn),
        sg.VSeperator(),
        sg.Column(picohOutputColumn),
        sg.VSeperator(),
        sg.Column(resultsOutputColumn)],
        ]

        # create the window and show it without the plot
    sg.theme("Reds")
    window = sg.Window('SEAI',layout, location=(100, 100),finalize=True)

    return window

async def main_window():
    global emotion_labels
    emotion_labels = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Sadness', 'Surprise', 'Neutral']
    #Create Directory to save images as well as analysis
    downloads_path = os.path.join(Path.home(), "Downloads\\pyFeatData\\" + datetime.now().strftime('%Y%m%d %H%M%S'))
    os.mkdir(downloads_path)
    
    # Create Main Window
    window = create_main_window()
    inst = vlc.Instance()
    player = inst.media_player_new()
    player.set_hwnd(window['-VID_OUT-'].Widget.winfo_id())

    # Initialize objects needed for interprocess communication
    lifoQueue = asyncio.LifoQueue() #Frames Queues
    actionQueue = asyncio.Queue() # Actions Queue reacting to emotions
    evStop = Event() # Create event to tell threads to stop
    analyzingEvent = Event() # When set the app is doing a resource intensive task no point doing anything else    
    # Bring Picoh to Life
    tPicohLoop = Thread(target=forever_funct, args=(evStop,))
    tPicohLoop.start()
    talk_funct()     # Picoh Introduction Message

    # Start Asynchronous Processes to Capture Frame, Save Frame, Detect Emotions, Show Emotion/SEAI gives advice
    await asyncio.wait([captureAndSaveFrame(lifoQueue, actionQueue, window, player, downloads_path, evStop, analyzingEvent),detectAndShowEmotion(lifoQueue, actionQueue, window, player, downloads_path, evStop, analyzingEvent)])
    
    # Window was closed.. stop all threads and clean up
    evStop.set()
    tPicohLoop.join()
    picoh.reset()
    picoh.wait(1)
    picoh.close()
    cv2.destroyAllWindows()


"""
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
"""
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

def create_account():
    global selected_theme
    global seai_users
    global userfile

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
                new_user = {}
                new_user['password'] = values['-password-']
                new_user['username'] = values['-username-']
                if values['-email-'] != values['-remail-']:
                    sg.popup_error("Error: Emails dont match", font=16)
                    continue
                elif values['-email-'] == values['-remail-']:
                    new_user['email'] = values['-email-']
                    seai_users[new_user['username']]= new_user
                    new_user['resources'] = [
                            ['All', 'Relaxing Music', 'File', 'Resources/RelaxingMusic.mp3' ], 
                            ['All', 'Breathing Exercise Video', 'File', 'Resources/Video.mp4' ], 
                            ['All', 'Breathing Exercises', 'Web', 'https:/calm.com/breathe' ], 
                    ]
                    progress_bar()
                    serialize(seai_users, userfile)
                    send_email(new_user['email'])
                    break
    window.close()
#create_account()


def login():
    global selected_theme
    global seai_users
    global current_user
    
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
        elif event == "Ok":
            if values['-usrnm-'] in seai_users.keys():
                user = seai_users[values['-usrnm-']]
                if user['password'] == values['-pwd-']:
                    sg.popup("Welcome! " + user['username'])
                    current_user = user
                    break
                else:
                    sg.popup("Invalid login. Try again")
            else:
                sg.popup("Your account does not exist, please create an account")
    window.close()

def send_email(receiver_email):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = ("1allarakhimr@hdsb.ca")
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


def start_window():
    #themes = sg.ListOfLookAndFeelValues()
    global seai_users
    global userfile
    global current_user
    global selected_theme

    userfile = 'User_data.json'
    selected_theme = 'Reds'
    seai_users = deserialize(userfile)
    current_user = None

    sg.ChangeLookAndFeel(selected_theme)
    layout = [
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
            if current_user is not None:
                break
        if event =='Create Account':
            create_account()

    if current_user is not None:
        asyncio.run(main_window())

    window.close()



"""
                            if values['cbSaveVideo'] == True:
                                if tFileSave == None:
                                    evFileSaveStop.clear()
                                    tFileSave = Thread(target=CaptureVideoToFile, args=(downloadsPath+'\\' + emotion_labels[max_emotion_index] +'_output_' + datetime.now().strftime('%H%M%S') + '.avi', evFileSaveStop,))
                                    tFileSave.start()
                            if tFileSave != None:
                                evFileSaveStop.set()
                                tFileSave.join()
                                tFileSave = None
                            values['cbSaveVideo'] = saveVideoVal
"""
start_window()
