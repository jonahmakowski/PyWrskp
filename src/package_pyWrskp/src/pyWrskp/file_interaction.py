import json


def read_file(path):
    try:
        with open(path) as json_file:
            info = json.load(json_file)
        return info
    except FileNotFoundError:
        return None

def write_file(path, save):
    with open(path, 'w') as outfile:
        json.dump(save, outfile)
