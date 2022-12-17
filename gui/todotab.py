
import tkinter as tk
from tkinter import ttk
import re
# from setting.settingmanager import *
from core.eventhandler import *
from xtk.scrollframe import *

class TaskSummaryInfo(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        super(TaskSummaryInfo, self).__init__(*args, **kwargs)
        # self['background'] = 'gray'
        self['padx'] = 5
        self['pady'] = 5
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

        self.ui_project = tk.StringVar(value = '[Project Name]')
        self.project_label = tk.Label(self,textvariable=self.ui_project)
        self.project_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_due_day = tk.StringVar(value = '[Due Day]')
        self.due_day_label = tk.Label(self,textvariable=self.ui_due_day)
        self.due_day_label.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.E)
        row_cnt += 1

        button_frame = tk.Frame(self)
        button_frame.grid(row = row_cnt, column = 0, columnspan=2, sticky = tk.E)

        self.view_btn = tk.Button(button_frame, text = 'View')
        self.view_btn.pack(side=tk.RIGHT)

    def setInfo(self, name = None, priority = None, project = None, due_day = None):
        if name is not None:
            self.ui_name.set(name)
        if project is not None:
            self.ui_project.set(project)
        if priority is not None:
            self.ui_priority.set(priority)
        if due_day is not None:
            self.ui_due_day.set(due_day)

class TODOTab(tk.Frame):
    def __init__(self, event_handler, *args, **kwargs):
        super(TODOTab, self).__init__(*args, **kwargs)

        self.event_handler = event_handler
        # self.event_handler.registEvent(Event.Record, self.rev_Record, EventHandler.OnAction)
        # self['background'] = 'dark gray'

        ## Gui Setup
        #############################3
        # Create the VerticalScrolledFrame
        vs_frame = VerticalScrolledFrame(self)
        vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)
        self.scrollframe = vs_frame.interior

        # Fake data
        for each_idx in range(0, 200):
            tmp_task = TaskSummaryInfo(self.scrollframe)
            tmp_task.setInfo(name = 'Task_'+each_idx.__str__())
            tmp_task.pack(fill=tk.X, expand=True, padx = 5, pady = 3)


        ## Event Setup
        #############################3

