#import os

def speak(text):
    #os.system('say "{}"'.format(text))
    pass

def script_helper(script, actor, show_cue=False):
    for line in script:
        if line['actor'] == actor:
            input("Psst, it's your line!" if show_cue else '')
            print(line['actor'], line['line'])
        else:
            print()
            print(line['actor'], line['line'])
            speak(line['line'])

def load_script(path='script_raw.txt'):
    with open(path, 'r') as f:
        text = f.readlines()

    script = []

    for line in text:
        line = line.strip()
        script.append({'actor': line.split(': ')[0], 'line': line.split(': ')[1]})

    return script

if __name__ == '__main__':
    script_helper(load_script(), 'Jonah')
