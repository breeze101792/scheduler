import tkinter as tk
from tkinter import ttk
# from setting.settingmanager import *

class AddProjectWin(tk.Toplevel):
    def __init__(self, event_handler, *args, **kwargs):

        # __init__ function for class Tk
        # tk.Tk.__init__(self, *args, **kwargs)
        super(AddProjectWin, self).__init__(*args, **kwargs)
        self.title('Add New Project')
        self.protocol("WM_DELETE_WINDOW", self.closeWindow)

        ## Vars frame
        #################################
        self.event_handler = event_handler

        ## Side column frame
        #################################
        # sidebar_frame = tk.Frame(self, borderwidth=1) 
        main_frame = tk.Frame(self, borderwidth=0) 
        main_frame.config(highlightbackground='black')
        main_frame.pack(side = "top", fill='both', expand = True)
        main_frame.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)

        row_cnt = 0

        self.task_name_label = tk.Label(main_frame,textvariable='Name')
        self.task_name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_task_name = tk.StringVar(value = '[Task Name]')
        self.task_name_entry = tk.Entry(main_frame,textvariable=self.ui_task_name)
        self.task_name_entry.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.E)
        row_cnt += 1

        self.withdraw()
    def openWindow(self):
        self.deiconify()
    def closeWindow(self):
        self.withdraw()
    def quit(self):
        self.withdraw()
