import json  # this is a library

# This char "#" makes the rest of the line a comment and the computer ignores it

"""This is a other way to right comments
as this can be many lines"""

print()  # prints the item in the bracket

var1 = input('? str')  # takes input from the question put in the bracket in this case '? str' (this saves as a string)

var2 = int(input('? int'))
'''takes input from the question put in the bracket in this case '? int' (this saves as a int), the int() part takes the
 input and turns it into an int, if it is a word, like "Hello", it will return an error, if it is a float like 0.5 it 
 will also return an error'''

var3 = float(input('? float'))
'''takes input from the question put in the bracket in this case '? float' (this saves as a float), the float() part
takes the input and turns it into a float, if it is a word, like "Hello", it will return an error, if it is a int
like 1 it will make the int, 1 into 1.0'''

var4 = str(1 + 2)  # this will add 1 + 2 and save it as a string, so this would look like "3" in string form

var5 = 0  # makes a var that is = to the integer 0

var6 = 'Hello World'  # makes a var that is = to the string "Hello world"

var7 = 0.5  # makes a var that is = to the float 0.5

var8 = True  # this is a boolean value, True or False (it has to start with a capitol in python)

var9 = {'first name': 'Jonah',
        'middle name': 'Werner',
        'last name': 'Makowski',
        'age': 11,
        'grade': 6,
        'firends': ['Jacob',
                    'Phinn',
                    'Liam',
                    'Rafa',
                    'Ben G',
                    'Hannah']}
'''This is a dictonary, what it is is like a list with a key that is instead of a number what is in the string
the item the key is = to is anything, a list, a string, a int, a list, a dictonary, or a float.'''

var10 = [var1, var2, var3, var4, var5, var6, var7, var8]  # This makes a var = to a list of all of the other vars

for i in range(3):  # means do 3 times "i" is a counter
    print('hi')

for item in var10:  # means for every item in var10 (a list), do this, item is the current item that is going through
    print(item)

while True:  # this is a while statment and True can be reaplaced with other objects
    var5 += 1  # adds and equals 1
    if var5 == len(var10):
        # many things here, if statments are just as they sound, len() counts the number of objects in a list
        print('the number of objects in var9 are {}'.format(var5))  # .format replaces {} with the object in the brakets
        break  # this cuts out of a loop

with open('hello.txt', 'w') as outfile:  # how to save a file to the file named "hello.txt"
    json.dump('Testing message', outfile)  # this will save "Testing message" to a txt file

with open('hello.txt') as json_file:
    print(json.load(json_file))  # this will print the info in a file


def fuction():  # this is a fuction in the () you can put in info so that it can get info
    print('fuction testing')  # you have to start the fuction name with a lowercase letter


fuction()  # this is how to call up a fuction


class Testing:  # this is how to make a class
    def __init__(self, info):
        # this is needed in any class it is what happens when the class is first called on info is a paremater
        self.info = info  # this saves info as a file that you can use anyware in the class
    
    def print_info(self):  # this is a fuction that prints self.info
        print(self.info)


testing = Testing('Hello')  # this is how to call a class
testing.print_info()  # this is how to call a class fuction
        