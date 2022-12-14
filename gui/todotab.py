
import tkinter as tk
from tkinter import ttk
import re
# from setting.settingmanager import *
from core.eventhandler import *

class TaskInfo(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(TaskInfo, self).__init__(*args, **kwargs)
        # self['background'] = 'gray'
        row_cnt = 0
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)

        self.ui_name = tk.StringVar(value = '[Task Name]')
        self.name_label = tk.Label(self,textvariable=self.ui_name)
        self.name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_priority = tk.StringVar(value = '[Priority]')
        self.priority_label = tk.Label(self,textvariable=self.ui_priority)
        self.priority_label.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.E)
        row_cnt += 1

        self.ui_proj_name = tk.StringVar(value = '[Project Name]')
        self.proj_name_label = tk.Label(self,textvariable=self.ui_proj_name)
        self.proj_name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_due_day = tk.StringVar(value = '[Due Day]')
        self.due_day_label = tk.Label(self,textvariable=self.ui_due_day)
        self.due_day_label.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.E)

        row_cnt += 1

class TODOTab(tk.Frame):
    def __init__(self, event_handler, *args, **kwargs):
        super(TODOTab, self).__init__(*args, **kwargs)

        self.event_handler = event_handler
        # self.event_handler.registEvent(Event.Record, self.rev_Record, EventHandler.OnAction)
        # self['background'] = 'dark gray'

        ## Gui Setup
        #############################3
        canvas = tk.Canvas(self)
        # self.scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)

        # self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y, expand=True)
        # self.scrollbar.grid(row = 0, column = 1,sticky=tk.N+tk.S ,)

        # Fake data
        for each_idx in range(0, 20):
            tmp_task = TaskInfo(self)
            tmp_task.pack(fill=tk.X, expand=True)


        ## Event Setup
        #############################3

