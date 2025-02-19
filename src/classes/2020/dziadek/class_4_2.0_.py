import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Application(tk.Frame):
    def __init__(self, name, save_loc, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()
        self.name = name
        self.save_loc = save_loc
    def createWidgets(self):
        self.txtEdit = tk.Text(self)
        self.btnFrame = tk.Frame(self)
        self.btnOpen = tk.Button(self.btnFrame, text='Open', command=self.openFile)
        self.btnSaveas = tk.Button(self.btnFrame, text='Save as', command = self.saveFile)
        self.btnquit = tk.Button(self.btnFrame, text='Close', command = self.master.destroy)
        self.btnsave = tk.Button(self.btnFrame, text = 'save', command = self.save)
        
        self.txtEdit.grid(row=0, column=1, sticky='nsew')
        self.btnFrame.grid(row = 0, column=0, sticky='ns')
        self.btnOpen.grid(row=0, column=0, sticky= 'ew')
        self.btnSaveas.grid(row=1, column=0, sticky= 'ew')
        self.btnsave.grid(row=2, column=0, sticky= 'ew')
        self.btnquit.grid(row=3, column=0, sticky='ew')
    def openFile(self):
        print('open in TXT folder only!!!')
        self.fp = askopenfilename(filetypes=[('all files that work with this code', ['*.py', '*.txt', '*.docx']), ('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')])
        self.name = self.fp[35:]
        if not self.fp:
            return
        self.txtEdit.delete(1.0, tk.END)
        with open(self.fp, 'r') as inFile:
            txt = inFile.read()
            self.txtEdit.insert(tk.END, txt)
    def saveFile(self):
        self.fp = asksaveasfilename(filetypes=[('all files that work with this code', ['*.py', '*.txt', '*.docx']), ('Text Files', '*.txt'), ('Python Files', '*.py'), ('All Files', '*.*')])
        self.name = self.fp[len(self.save_loc):]
        if not self.fp:
            return
        with open(self.fp, 'w') as outFile:
            txt = self.txtEdit.get(1.0, tk.END)
            outFile.write(txt)
    def save(self):
        with open(save_loc + self.name, "w") as f:
            try:
                txt = self.txtEdit.get(1.0, tk.END)
                f.write(txt)
                print('FYI it saved')
            except:
                print('FYI, your file did not save')
save_loc = '/home/jonah/Thonny files/TXT_files/' # change to folder name where you want auto saves
root = tk.Tk()
root.title('Text Editer')
root.rowconfigure(0, minsize =800, weight = 1)
root.columnconfigure(1, minsize =600, weight=1)
app = Application(None, save_loc, master=root)
app.mainloop()