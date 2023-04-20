print('Way 1')  # Way I think that John wants us to use

star = ' *'

for line in range(1, 5):
    for d in range(line):
        print(star, end='')
    print()


'''

Basicly, how this works is:
line = 1, 2, 3, 4
then line is but into the range loop,
decieding how many stars are printed on that line.
I used the "end=''" paramater so that it all prints on the same line.
The print() command you see at the end is so that the next line of *s is printed on a new line

'''

print('Way 2')  # Way I would use before this class (since I did not know about the end paramater in the print function)

star = ' *'

for line in range(4):
    print(star)
    star += ' *'

'''

How this works, is that it prints the variable star, and then within each looping,
it adds anouther " *" to the variable (thats what the star += " *" command does)
so the variable looks like this:
first print: " *"
second print: " * *"
third print: " * * *"
fourth print: " * * * *"

'''
