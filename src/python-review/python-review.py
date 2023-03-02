import time


class Class: # Information About Classes
    def __init__(self, inp):
        # All classes need an __init__ function
        # Any input parameters put in this function can be inputted when the class is called upon (such as inp)
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
