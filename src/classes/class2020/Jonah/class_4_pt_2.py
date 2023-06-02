import class_4_pt_1
import tkinter as tk
df_save_loc = '/home/jonah/Thonny files/TXT_files/'  # change to folder name where you want auto saves as def
df_name = 'testing'  # you can change def save name
root = tk.Tk()
root.title('Text Editer')
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=600, weight=1)
app = class_4_pt_1.Application(df_name, df_save_loc, master=root)
app.mainloop()
