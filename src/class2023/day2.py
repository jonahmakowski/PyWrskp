while True:
    amount = input('How many lines would you like?\n')
    if amount.isdigit():
        amount = int(amount)
        break
    else:
        print('You really are a BIG student, that is not a number!',
              'I asked how many lines you wanted and you said "{}"!'.format(amount),
              'Really, you should learn what a number is!',
              sep='\n',
              end='\n\n')


'''

All this part does is set how many lines there will be.

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

input('Press enter to countinue')
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

print('Extra Assignment')

input('Press enter to countinue')
print('Way 1')  # Did this before I saw the assignment, does not really follow the critrea of the extra assignment

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

I made this very compicated for some reason, way 2 is a much better way to do this.

-----------------------------------------------------------------------------------------------------------

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

input('Press enter to countinue')
print('Way 2')  # done after I saw the assignment, follows the critrea

space = ' '
star = ' *'

for line in range(1, amount+1):
    for i in range(amount - line):
        print(space, end='')
    for i in range(line):
        print(star, end='')
    print()

'''

**Assuming amount is 5**

How this works is first space is print 5 times, then a star is printed 1 time, then a new line
                                       ^                               ^
                                       |                               |
                                       A                               B
Then remove one from A and add one to B

Repeat five times.

'''

input('Press enter to countinue')
print('Way 3')  # Upside down pyriamd

space = ' '
star = ' *'

for line in range(amount):
    for i in range(line):
        print(space, end='')
    for i in range(amount - line):
        print(star, end='')
    print()

input('Press enter to continue')
print('Way 4')

space = ' '
star = ' *'
amount_of_space = amount + 1
amount_of_star = 0

for line in range(1, amount+1):
    amount_of_space -= 1
    amount_of_star += 1
    print(space*amount_of_space+star*amount_of_star)
