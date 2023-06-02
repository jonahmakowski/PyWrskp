import tkinter as tk

class app(tk.Frame):
    def __init__(self, i, master=None):
        super().__init__(master)
        self.master = master
        self.i = i
        self.i_2 = i
        self.i_3 = i
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.btnFrame = tk.Frame(self)
        self.btnpaint = tk.Button(self.btnFrame, text='Paint', command = self.paint)
        self.btnpaint_2 = tk.Button(self.btnFrame, text= 'Paint v2', command = self.paint_2)
        self.btnhome = tk.Button(self.btnFrame, text='Home stuff', command=self.home)
        self.btntextedit = tk.Button(self.btnFrame, text='text editer', command=self.text_edit)
        self.btnclose = tk.Button(self.btnFrame, text='close', command=self.master.destroy())
        self.btns = [self.btnpaint, self.btnpaint_2, self.btnhome, self.btntextedit, self.btnclose]
        
        self.btnFrame.grid(row = 0, column=0, sticky='ns')
        i = 0
        for item in self.btns:
            item.grid(row=i, column = 0, sticky='ew')
            i += 1
    def paint(self):
        import Class_one
        if self.i != 0:
            Class_one.draw()
        self.i += 1
    def paint_2(self):
        import class_2
        if self.i_2 != 0:
            class_2.paint()
        self.i_2 += 1
    def home(self):
        import class_3_homework as class_3
        if self.i_3 != 0:
            class_3.extra()
        self.i_3 += 1
    def text_edit(self):
        import Class_4 as class_4
        self.df_save_loc = '/home/jonah/Thonny files/TXT_files/' # change to folder name where you want auto saves as def
        self.df_name = 'testing' # you can chnage def save name
        self.root_2 = tk.Tk()
        self.root_2.title('Text Editer')
        self.root_2.rowconfigure(0, minsize =800, weight = 1)
        self.root_2.columnconfigure(1, minsize =600, weight=1)
        self.app_2 = class_4.Application(df_name, df_save_loc, master=root_2)
        self.app_2.mainloop()

root = tk.Tk()
i = 0
root.rowconfigure(0, minsize =9999, weight = 1)
root.columnconfigure(1, minsize =9999, weight=1)
app = app(i, master=root)
app.mainloop()