def run_code(code):
    exec(code)

code = ''
print('what is your code (enter = new line):')

while True:
    cod = input()
    if cod == '':
        break
    code += cod + '\n'

run_code(code)