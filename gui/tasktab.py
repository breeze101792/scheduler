import tkinter as tk
from tkinter import ttk
import re
# from setting.settingmanager import *
from core.eventhandler import *
from xtk.scrollframe import *

class TaskTab(tk.Frame):
    def __init__(self, event_handler, project_manager, container, *args, **kwargs):
        super(TaskTab, self).__init__(container, *args, **kwargs)
        self.container = container

        ## Vars init
        #############################3
        self.event_handler = event_handler
        # self.event_handler.registEvent(Event.Record, self.rev_Record, EventHandler.OnAction)
        self.project_manager = project_manager


        ## Gui Setup
        #############################3
        self['background'] = 'dark gray'

        # Create the VerticalScrolledFrame
        vs_frame = VerticalScrolledFrame(self)
        vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)
        self.scrollframe = vs_frame.interior
        row_cnt = 0

        # self.ui_name = tk.StringVar(value = '[Task Name]')
        # self.name_label = tk.Label(self.scrollframe,textvariable=self.ui_name)
        # self.name_label.pack(fill=tk.X, expand=True, padx = 5, pady = 3)

        # self.ui_name = tk.StringVar(value = '[Task Name]')
        # self.name_label = tk.Label(self.scrollframe,textvariable=self.ui_name)
        # self.name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        # self.ui_priority = tk.StringVar(value = '[Priority]')
        # self.priority_label = tk.Label(self.scrollframe,textvariable=self.ui_priority)
        # self.priority_label.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.E)
        # row_cnt += 1

        # self.ui_project = tk.StringVar(value = '[Project Name]')
        # self.project_label = tk.Label(self.scrollframe,textvariable=self.ui_project)
        # self.project_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        # self.ui_due_day = tk.StringVar(value = '[Due Day]')
        # self.due_day_label = tk.Label(self.scrollframe,textvariable=self.ui_due_day)
        # self.due_day_label.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.E)
        # row_cnt += 1

        # Button
        button_frame = tk.Frame(self.scrollframe)
        button_frame.pack(side = tk.BOTTOM, fill = tk.Y)

        self.view_btn = tk.Button(button_frame, text = 'Close', command=self.on_tabClose)
        self.view_btn.pack(side=tk.RIGHT)


        ## Event Setup
        #############################3
    def on_tabClose(self):
        # self.forget()
        self.container.forget(self)
