class docs:
    def __init__(self):
        self.file_name = input('What is the file name?')
    
    def read(self):
        file = open(self.file_name, 'r')
        print(file.read())
        return file
    
    def create(self, pr=True, add=None, text=None):
        text = ''
        file = open(self.file_name, 'w')
        if pr:
            print('What would you like to write in your file')
        if text != None:
            while True:
                temp_text = input('')
                if temp_text == ' ':
                    break
                ttemp_text = temp_text + '\n'
                text += ttemp_text
        if add != None:
            text += add.read()
        file.write(text)
    
    def add(self):
        file = self.read()
        self.create(pr=False, add=file)

doc = docs()
info = input("Would you like read, create, or add (for add, you need to have a file and you can't remove old sections)")
if info == 'add':
    doc.add()
elif info == 'create':
    doc.create()
elif info == 'read':
    doc.read()