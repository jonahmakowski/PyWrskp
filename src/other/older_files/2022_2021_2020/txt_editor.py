class TxtReader:
    def __init__(self):
        self.file_loc = input('Enter the path for this .txt file\nOr enter create for a new file')
        if self.file_loc == 'create':
            self.file_loc = input('What is the path for the new file you want to make')
            self.write('', self.file_loc)
            print('An empty file should be created at that loc.')
        self.mainloop()
    
    def mainloop(self):
        while True:
            do = input('What do you want to do?')
            if do == 'wipe & write' or do == 'w&w':
                self.wipe_and_write()
                break
            elif do == 'add' or do == 'a':
                self.add()
                break
            elif do == 'read' or do == 'r':
                self.show()
                break
            else:
                print('{} is not an option'.format(do))
                print('Here are the options:')
                print('\t"wipe & write"')
                print('\t\t"w&w"')
                print('\t"add"')
                print('\t\t"a"')
                print('\t"read"')
                print('\t\t"r"')
    
    def show(self):
        write = self.read(self.file_loc)
        print('The current file is:')
        print(write)
    
    def add(self):
        write = self.read(self.file_loc)
        print('The current file is:')
        print(write)
        write_add = input('What do you wish to add? (use "\ n"\n')
        write_all = write + write_add
        self.write(write_all, self.file_loc)
    
    def wipe_and_write(self):
        write = input('What do you wish to write?\n')
        self.write(write, self.file_loc)
    
    def read(self, loc):
        with open(loc, 'r') as inFile:
            txt = inFile.read()
        return txt
    
    def write(self, item, loc):
        with open(loc, 'w') as outFile:
            outFile.write(item)
    
txt_reader = TxtReader()