def load_script(path='script_raw.txt'):
    with open(path, 'r') as f:
        text = f.readlines()

    script = []

    for line in text:
        line = line.strip()
        script.append({'actor': line.split(': ')[0], 'line': line.split(': ')[1]})

    return script

if __name__ == '__main__':
    print(load_script())
