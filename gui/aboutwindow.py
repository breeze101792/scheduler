import tkinter as tk
from tkinter import ttk
# from setting.settingmanager import *

class About(tk.Toplevel):
    # __init__ function for class AdvcanceSetting
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        # tk.Tk.__init__(self, *args, **kwargs)
        super(About, self).__init__(*args, **kwargs)
        self.title('About')
        self.protocol("WM_DELETE_WINDOW", self.closeWindow)

        about_string = '''
Scheduler
'''
        # about_string = about_string + 'Current version: {}'.format(Setting.Version)

        ## Side column frame
        #################################
        # sidebar_frame = tk.Frame(self, borderwidth=1) 
        about_frame = tk.Frame(self, borderwidth=0) 
        about_frame.config(highlightbackground='black')
        about_frame.pack(side = "top", fill='both', expand = True)

        about_frame.rowconfigure(0, weight=1)
        about_frame.columnconfigure(0, weight=1)

        about_text = tk.Text(about_frame, borderwidth=1)
        # Font_tuple = (Setting.Terminal.font['family'], Setting.Terminal.font['size'], Setting.Terminal.font['options'])
        # about_text.configure(font = Font_tuple)
        about_text.bind("<KeyPress>", lambda event: "break")
        about_text.insert('end', about_string)
        # about_text.pack(side = "top", fill='both', expand = True)
        about_text.grid(row = 0, column =0, sticky=tk.E+tk.W+tk.N+tk.S)
        about_text.config(state='disabled')

        self.scrollbar = tk.Scrollbar(about_frame, command=about_text.yview)
        self.scrollbar.grid(row = 0, column = 1,sticky=tk.N+tk.S)
        about_text['yscrollcommand'] = self.scrollbar.set

        # close_button = tk.Button(self, text="Close", command = self.closeWindow)
        # close_button.pack(side = "bottom")

        self.withdraw()
    def openWindow(self):
        self.deiconify()
    def closeWindow(self):
        self.withdraw()
    def quit(self):
        self.withdraw()
