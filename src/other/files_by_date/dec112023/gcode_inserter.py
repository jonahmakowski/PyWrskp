# Code that inserts a gcode command at the start of each layer.

command = ''
path = ''
sign = ''

while command == '':
    command = input('Enter command: ')

while path == '':
    path = input('Enter gcode path: ')

while sign == '':
    sign = input('Enter new layer sign that your slicer uses: ')

command += '\n'

gcode_file = open(path)

gcode = gcode_file.readlines()

gcode_file.close()

line = 0

while line != len(gcode) - 1:
    for line_loop in range(line, len(gcode)-1):
        line = line_loop
        if sign in gcode[line_loop]:
            layer_num = gcode[line_loop].split(sign[-1])
            layer_num = layer_num[-1]
            print('Found layer {}'.format(layer_num))
            gcode.insert(line_loop+1, command)
            break
    line += 1

with open(path, 'w') as gcode_file:
    gcode_file.writelines(gcode)
