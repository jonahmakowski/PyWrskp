import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.txtEdit = tk.Text(self)
        self.btnFrame = tk.Frame(self)
        self.btnOpen = tk.Button(self.btnFrame, text='Open', command=self.openFile)
        self.btnSave = tk.Button(self.btnFrame, text='Save as', command = self.saveFile)
        
        self.txtEdit.grid(row=0, column=1, sticky='nsew')
        self.btnFrame.grid(row = 0, column=0, sticky='ns')
        self.btnOpen.grid(row=0, column=0, sticky= 'ew')
        self.btnSave.grid(row=1, column=0, sticky= 'ew')
    def openFile(self):
        fp = askopenfilename(filetypes=[('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')])
        if not fp:
            return
        self.txtEdit.delete(1.0, tk.END)
        with open(fp, 'r') as inFile:
            txt = inFile.read()
            self.txtEdit.insert(tk.END, txt)
    def saveFile(self):
        fp = asksaveasfilename(filetypes=[('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')])
        if not fp:
            return
        with open(fp, 'w') as outFile:
            txt = self.txtEdit.get(1.0, tk.END)
            outFile.write(txt)
root = tk.Tk()
root.title('Text Editer')
root.rowconfigure(0, minsize =800, weight = 1)
root.columnconfigure(1, minsize =600, weight=1)
app = Application(master=root)
app.mainloop()