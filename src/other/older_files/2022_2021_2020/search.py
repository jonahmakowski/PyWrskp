import tkinter as tk
class search(tk.Frame):
    def __init__(self, items, master=None):
        super().__init__(master)
        self.master = master
        self.items = items
        self.pack()
        self.cteate()
    def create(self):
        self.entry1 = tk.Entry(self.master, justify='right')
        self,entry1.place(x=0, y=100, width=1000, height=25)
        
