import os

def speak(text):
    """
    Uses the system's text-to-speech functionality to speak the given text.

    Args:
        text (str): The text to be spoken.
    """
    os.system('say "{}"'.format(text))

def script_helper(script, actor, after_pause=False):
    """
    A helper function to assist with memorizing scripts by printing lines spoken by a specific actor.

    Args:
        script (list of dict): The script to be memorized, where each line is represented as a dictionary 
                               with keys 'actor' and 'line'.
        actor (str): The name of the actor whose lines are to be prompted for input.
        after_pause (bool, optional): If True, pauses for input after printing the actor's line. Defaults to False.

    Returns:
        None
    """
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
    """
    Loads a script from a text file and parses it into a list of dictionaries.

    Each line in the text file is expected to be in the format "actor: line".
    Lines that do not follow this format are assumed to be stage cues.

    Args:
        path (str): The path to the text file containing the script. Defaults to 'script_raw.txt'.

    Returns:
        list: A list of dictionaries, each containing 'actor' and 'line' keys.
    """
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
