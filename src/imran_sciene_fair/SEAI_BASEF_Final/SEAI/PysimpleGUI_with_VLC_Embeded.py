from pathlib import Path

try:
    import vlc
except:
    from os import environ
    vlc_path = 'C:\Program Files\VideoLAN\VLC'
    environ['PATH'] += ';' + vlc_path
    import vlc
import PySimpleGUI as sg

Instance = vlc.Instance()
player = Instance.media_player_new()

sg.theme("DarkBlue")

layout = [
    [sg.Graph((640, 480), (0, 0), (640, 480), key='-CANVAS-')],     # OK if use [sg.Canvas(size=(640, 480), key='-CANVAS-')],
]
window = sg.Window('Emotion Window', layout, finalize=True)

video_panel = window['-VID_OUT-'].Widget.master
# set the window id where to render VLC's video output
h = video_panel.winfo_id()  # .winfo_visualid()?
player.set_hwnd(h)
m = Instance.media_new(str("Resources/video.mp4"))  # Path, unicode
player.set_media(m)
player.play()


while True:

    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-IN-':
        video = values[event]
        if Path(video).is_file():
            m = Instance.media_new(str(video))  # Path, unicode
            player.set_media(m)
            player.play()

player.stop()
window.close()
