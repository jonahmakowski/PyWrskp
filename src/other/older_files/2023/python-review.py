print('Information About Classes')


class Class:  # Information About Classes
    def __init__(self, inp):
        # All classes need an __init__ function
        # Any input parameters (like inp) put in this function can be inputted when the class is called upon (Line 23)
        # When a Class is defined it runs the __init__ function
        self.inp = inp
        # When using a variable such as self.inp that has the "self" part, it means that the variable is usable
        # all over the class
        self.start()
        # This runs the method start
        # To call a method you use self.METHODNAME()

    def start(self):
        print(self.inp)
        # This is a method
        # A method is basically a function within a class that can be called upon in the class
        # To call a method you use self.METHODNAME()


c = Class('Testing')
# This is how you call upon a class, doing this will run the class' __init__ function
# 'Testing' is where you would input the parameters so in this case
# inp (The name of the parameter used in this example) = 'Testing'

# Information About Functions

print()
print()
print('Information About Functions')


def function(parameter):
    # Parameter is a input that you can get from outside the function when it is called upon on lines 45 - 47
    # A function should be used when:
        # A block of code is used several times
        # If you want to make things simpler, and easier to read and understand
    # learning to call upon it is lines 40 - 44
    print(parameter)
    return parameter
    # this last command "return parameter" will be explained on line ___


# Either This
p = function('parameter')
# Or This:
function('parameter')
# is how you call upon a function

# To explain the command on line 36 and the "p =" on line 40:
# What return does is it gives a value back to where it was called upon
# "p =" Takes that value and puts it in "p"


# Variables and their types in python:

print()
print()
print('Variables and their types in python')

string_example = 'String'  # String
string_example = "String"  # String
# These two commands do the same thing
# Strings are used with text, but can also contain numbers

integer_example = 10  # Integer
# integers are whole numbers

float_example = 10.1  # Float
# Floats are decimal numbers

list_example = ['String', 10, 10.1, string_example, integer_example, float_example]  # List
# Lists can contain any other type of variable and are a list
# values from the list can be called like this:
list_item = list_example[0]
# In this case, "list_item" would be equal to 'String' because that is what is number 0 in the list
# This is because the first item in the list is 0, then it is 1 2 3 4 5 etc

dictionary_example = {'String': 'string', 'int': 10, 'float': 10.1}
# dictionaries are similar to lists, but is be called differently
# To call a list you do this:
dictionary_item = dictionary_example['int']
# in this case "dictionary_item" would equal 10
# This is because the index for a dictionary is not a number, but a string value, and under the index 'int' is 10


# if then else:
print()
print()
print('if then else')

if 1 + 1 == 2:  # This asks if 1 + 1 = 2
    print('True')
elif 2 + 2 == 4:  # Although this will never happen (in this case), should the previous if be false,
    # it will ask this question if 2 + 2 = 4
    print('True 2')
else:  # If the ifs it lines up with are all false, this shall happen
    print('False')


# loops
print()
print()
print('Loops:')

for i in range(10):  # this is a loop 10, so it repeats 10 times
    print(i)  # i is the counter in this case (it will start at 0)

li = ['L', 'D', 5]

for i in li:  # This is also a list, but for item in a list
    print(i)  # i is the item in the list that it is currently on in this case

i = 0

while True:  # this will repeat while True is true (so forever) or until a break command is used
    # You can replace True with any variable as well
    print(d)
    i += 1
    if i > 4:
        break  # this stops the loop that the command is in
