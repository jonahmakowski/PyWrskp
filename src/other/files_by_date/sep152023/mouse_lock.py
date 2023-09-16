from pynput.mouse import Controller as MouseController
from pynput.keyboard import Listener, KeyCode

# Initialize the mouse controller
mouse = MouseController()

# Flag to track mouse lock state
mouse_locked = False

# Function to lock or unlock the mouse
def toggle_mouse_lock():
    global mouse_locked
    if not mouse_locked:
        mouse.press(MouseController.LEFT)
        mouse_locked = True
    else:
        mouse.release(MouseController.LEFT)
        mouse_locked = False

# Define the keyboard shortcut (in this case, the "Ctrl" key)
shortcut_key = KeyCode.from_char('ctrl')

# Register a hotkey to toggle mouse lock
def on_press(key):
    if key == shortcut_key:
        toggle_mouse_lock()

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
