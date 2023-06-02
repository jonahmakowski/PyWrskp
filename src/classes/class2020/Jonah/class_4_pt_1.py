import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


class Application(tk.Frame):
    def __init__(self, name, save_loc, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createwidgets()
        self.fp = save_loc + name

    def createwidgets(self):
        self.txtEdit = tk.Text(self)
        self.btnFrame = tk.Frame(self)
        self.btnOpen = tk.Button(self.btnFrame, text='Open', command=self.openfile)
        self.btnSaveas = tk.Button(self.btnFrame, text='Save as', command=self.savefile)
        self.btnquit = tk.Button(self.btnFrame, text='Close', command=self.master.destroy)
        self.btnsave = tk.Button(self.btnFrame, text='save', command=self.save)
        
        self.txtEdit.grid(row=0, column=1, sticky='nsew')
        self.btnFrame.grid(row=0, column=0, sticky='ns')
        self.btnOpen.grid(row=0, column=0, sticky='ew')
        self.btnSaveas.grid(row=1, column=0, sticky='ew')
        self.btnsave.grid(row=2, column=0, sticky='ew')
        self.btnquit.grid(row=4, column=0, sticky='ew')

    def openfile(self):
        testing = askopenfilename(filetypes=[('all files that work with this code', ['*.py', '*.txt', '*.docx']), ('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')])
        if not testing:
            return
        else:
            self.fp = testing
        self.txtEdit.delete(1.0, tk.END)
        with open(self.fp, 'r') as inFile:
            txt = inFile.read()
            self.txtEdit.insert(tk.END, txt)

    def savefile(self):
        testing = asksaveasfilename(filetypes=[('all files that work with this code', ['*.py', '*.txt', '*.docx']), ('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')])
        if not testing:
            return
        else:
            self.fp = testing
        with open(self.fp, 'w') as outFile:
            txt = self.txtEdit.get(1.0, tk.END)
            outFile.write(txt)
    def save(self):
        with open(self.fp, "w") as f:
            try:
                txt = self.txtEdit.get(1.0, tk.END)
                f.write(txt)
            except:
                print('FYI, your file did not save')

    def enter(self, info):
        self.txtEdit.insert(tk.END, info)
