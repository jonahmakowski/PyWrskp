import sys
import os
import threading
from subprocess import Popen


def exec_applescript(script):
    p = Popen(['osascript', '-e', script])


def process_file(filename):
    print('Processing file {}'.format(filename))  # Debug Message
    process_script = """-- Set the application to monitor and the message to display
                        set monitoredApp to "{}"
                        set displayMessage to "{}"
                        set showMessage to false

                        -- Function to check if the application is in the foreground
                        on isAppInForeground(appName)
                            tell application "System Events"
                                set frontApp to name of first application process whose frontmost is true
                            end tell
                            if frontApp is appName then
                                return true
                            else
                                return false
                            end if
                        end isAppInForeground
                        
                        -- Main loop to continuously check if the application is in the foreground
                        repeat while showMessage is false
                            if isAppInForeground(monitoredApp) then
                                activate
                                display dialog displayMessage buttons {"OK"} default button "OK"
                                -- Wait until the application is no longer in the foreground before checking again
                                set showMessage to true
                            end if
                            -- Check every second
                            delay 1
                        end repeat
                        """
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines
        lines = file.readlines()

    # Separate the first line from the rest
    first_line = lines[0]
    rest_of_lines = lines[1:]

    Popen(['rm', filename])

    exec_applescript(process_script.format(first_line.strip(), ''.join(rest_of_lines).strip()))


if __name__ == '__main__':
    files = list(os.walk('notes'))
    for file in files:
        path = ''
        for part in file:
            if not part:
                path += '/'
            else:
                if type([]) == type(part):
                    path += part[0]
                else:
                    path += part
        print(path)

        t = threading.Thread(target=process_file, args=(path,))
        t.start()
