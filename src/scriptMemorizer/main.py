import os

def speak(text):
    os.system('say "{}"'.format(text))

def script_helper(script, actor, show_cue=False):
    for line in script:
        if line['actor'] == actor:
            input("Psst, it's your line!" if show_cue else '')
            print(line['actor'], line['line'])
        else:
            print()
            print(line['actor'], line['line'])
            speak(line['line'])

if __name__ == '__main__':
    from script_formatter import load_script
    script_helper(load_script(), 'M2')
