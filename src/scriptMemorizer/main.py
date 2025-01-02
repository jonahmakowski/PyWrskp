import os

def speak(text):
    os.system('say "{}"'.format(text))

def script_helper(script, actor, after_pause=False):
    for line_num, line in enumerate(script):
        if line['actor'] == actor:
            input()
            print('{} of {}\t{}: {}'.format(line_num+1, len(script), line['actor'], line['line']))
            if after_pause:
                input()
        else:
            print()
            print('{} of {}\t{}: {}'.format(line_num+1, len(script), line['actor'], line['line']))
            speak(line['line'])

def load_script(path='script_raw.txt'):
    with open(path, 'r') as f:
        text = f.readlines()

    script = []

    for line in text:
        line = line.strip()
        if len(line.split(': ')) != 1:
            script.append({'actor': line.split(': ')[0], 'line': line.split(': ')[1]})
        else:
            script.append({'actor': 'Stage Cue', 'line': line})

    return script

if __name__ == '__main__':
    script_helper(load_script(), 'Knight', after_pause=True)
