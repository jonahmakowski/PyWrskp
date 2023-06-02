import json
import os

try:
    pyWrkspLoc = os.environ["PYWRKSP"]

except KeyError:
    pyWrkspLoc = os.environ["HOME"] + input('Since you do not have the PYWRSKP env var '
                                            '\nPlease enter the pwd for the pyWrskp repo not including the '
                                            '"home" section')


class ShoppingList:
    def __init__(self, py_wrskp):
        self.name = py_wrskp + '/docs/txt-files/shopping_list.txt'
        self.list = self.load()
        print('the current list is:')
        self.show()
        t = input('what would you like to do?')
        if t == 'add':
            self.add()
            print('The list is now:')
            self.show()
        elif t == 'rm':
            self.rm()
            print('The list is now:')
            self.show()
        self.save()

    def load(self):
        try:
            with open(self.name) as json_file:
                j = json.load(json_file)
        except FileNotFoundError:
            print('This file does not exist')
            exit(5)
        return j

    def add(self):
        item = input('What is the name of the object you want to add to your list?')
        self.list.append(item)

    def rm(self):
        item = input('What is the name of teh item you would like to remove, make sure this is right')
        if item == 'all':
            self.list = []
        else:
            for i in range(len(self.list)):
                if self.list[i] == item:
                    del self.list[i]
                    break

    def show(self):
        for item in self.list:
            print(item)

    def save(self):
        with open(self.name, 'w') as outfile:
            json.dump(self.list, outfile)


if __name__ == "__main__":
    shopping_list = ShoppingList(pyWrkspLoc)
