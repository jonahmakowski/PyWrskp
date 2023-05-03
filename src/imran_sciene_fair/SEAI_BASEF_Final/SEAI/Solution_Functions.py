import random
import webbrowser
from picoh import picoh
from pathlib import Path

try:
    import vlc
except:
    from os import environ
    vlc_path = 'C:\Program Files\VideoLAN\VLC'
    environ['PATH'] += ';' + vlc_path
    import vlc

def EmotionSolutions(emotionName, player, user):
    emotionResources = []
    for resource in user['resources']:
        if resource[0] == 'All' or resource[0] == emotionName :
            emotionResources.append(resource)
    selectedResource = random.choice(emotionResources)
    if selectedResource[2] == 'Web':
        BrowseUrl(selectedResource)
    elif selectedResource[2] == 'File':
        PlayMedia(player, selectedResource)

def BrowseUrl(resource):
    picoh.untillDone= picoh.say(resource[1])
    webbrowser.open_new(resource[3])
    picoh.wait(1)
    picoh.untillDone = picoh.say("You're Welcome")

def PlayMedia(player, resource):
    picoh.untillDone= picoh.say(resource[1])
    inst = player.get_instance()
    m = inst.media_new(resource[3])  # Path, unicode
    player.set_media(m)
    player.play()

"""
def PlayMedia(player, mediaFile):
    inst = player.get_instance()
    m = inst.media_new(mediaFile)  # Path, unicode
    player.set_media(m)
    player.play()
def AngerSolutions(player, user):
    angerFuncList = [RelaxingMusic, Breathing_Exercise_Video, Breathing_Exercise_Web]
    random.choice(angerFuncList)(player)
    print('Anger')

def SadSolutions(player, user):
    angerFuncList = [RelaxingMusic, Breathing_Exercise_Video, Breathing_Exercise_Web]
    random.choice(angerFuncList)(player)
    print('Sad')

def DisgustSolutions(player, user):
    angerFuncList = [RelaxingMusic, Breathing_Exercise_Video, Breathing_Exercise_Web]
    random.choice(angerFuncList)(player)
    print('Disgusted')

def HappySolutions(player, user):
    angerFuncList = [RelaxingMusic, Breathing_Exercise_Video, Breathing_Exercise_Web]
    random.choice(angerFuncList)(player)
    print('Happy')

def SurprisedSolutions(player, user):
    angerFuncList = [RelaxingMusic, Breathing_Exercise_Video, Breathing_Exercise_Web]
    random.choice(angerFuncList)(player)
    print('Surprised')

def FearSolutions(player, user):
    angerFuncList = [RelaxingMusic, Breathing_Exercise_Video, Breathing_Exercise_Web]
    random.choice(angerFuncList)(player)
    print('Fearful')

def NeutralSolutions(player, user):
    angerFuncList = [RelaxingMusic, Breathing_Exercise_Video, Breathing_Exercise_Web]
    random.choice(angerFuncList)(player)
    print('Boring')

def SadSolutions(player, user):
    angerFuncList = [RelaxingMusic, Breathing_Exercise_Video, Breathing_Exercise_Web]
    random.choice(angerFuncList)(player)
    print('Anger')

def RelaxingMusic(player):
    picoh.untillDone= picoh.say("Chill with some good music")
    picoh.wait(1)
    picoh.untillDone = picoh.say("You're Welcome")
    PlayMedia(player, 'Resources/RelaxingMusic.mp3')

def Breathing_Exercise_Video(player):
    picoh.untillDone= picoh.say("Breathing Exercise Video")
    picoh.wait(1)
    picoh.untillDone = picoh.say("You're Welcome")
    PlayMedia(player, 'Resources/video.mp4')

    # set the window id where to render VLC's video output

def Breathing_Exercise_Web(player):
    picoh.untillDone= picoh.say("Breathing Exercise")
    webbrowser.open_new('https:/calm.com/breathe')
    picoh.wait(1)
    picoh.untillDone = picoh.say("You're Welcome")

"""