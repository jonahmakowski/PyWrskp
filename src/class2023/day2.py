while True:
    try:
        amount = int(input('How many lines would you like?\n'))
        break
    except ValueError:
        print('That is not a number, try again.')
        print()


'''

All this part does is set how many lines there will be for the triangles.
All three ways will result in the same thing.

'''

print('Way 1')  # Way I think that John wants us to use

star = ' *'

for line in range(1, amount + 1):
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
The +1 on line 20 is because the range() command does not include the number given

'''

print('Way 2')  # Way I would use before this class (since I did not know about the end paramater in the print function)

star = ' *'

for line in range(amount):
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

print('Way 3')  # Kind of diffrent, more of a pyramid

star = []
for i in range(amount-1):
    star.append('   ')
star.append(' * ')
for i in range(amount-1):
    star.append('   ')

cur_index_r = amount - 1
cur_index_l = amount - 1

for line in range(amount):
    star[cur_index_r] = ' * '
    star[cur_index_l] = ' * '
    cur_index_l -= 1
    cur_index_r += 1
    for item in star:
        print(item, end='')
    print()

'''

How this works is that I used lists, a diffrent variable type.
To start I define an empty list (stars = []),
then I add the correct amount of spaces, to make the payramid start in the middle
After I add one star, to make the center point, then add more spaces again.
After that I define two variables, cur_index_l (current index left), and cur_index_r (current index right)
These two are used to count where the star should be added
Then I go into a loop that first adds stars to the index that is within cur_index_r, and then cur_index_l
(these variables start in the middle point)
After that I modify cur_index_l and cur_index_r to prepare them for the next line.
The second last thing I do in this loop, is start a second loop that prints all of the contents of star (the list), on
one line after that I print a new line, so that the next line of the pyraimd starts of on a new line

'''
