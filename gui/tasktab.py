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
        self.task_ins = None

        ## Gui Setup
        #############################3
        self['background'] = 'dark gray'

        # Create the VerticalScrolledFrame
        vs_frame = VerticalScrolledFrame(self)
        vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)

        self.scrollframe = tk.Frame(vs_frame.interior)
        self.scrollframe.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE)

        # self.scrollframe = vs_frame.interior
        self.scrollframe['background']='gray'
        row_cnt = 0

        # self.ui_name = tk.StringVar(value = '[Task Name]')
        task_name_label = tk.Label(self.scrollframe,text='Task Name:')
        task_name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = 'news')

        self.ui_task_name = tk.StringVar(value = '')
        self.task_name_entry = tk.Entry(self.scrollframe, textvariable = self.ui_task_name)
        self.task_name_entry.grid(row = row_cnt, column = 1, sticky = tk.W)
        row_cnt += 1

        project_name_label = tk.Label(self.scrollframe,text='Project Name:')
        project_name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_project_name = tk.StringVar(value = '')
        self.project_name_entry = tk.Entry(self.scrollframe, textvariable = self.ui_project_name)
        self.project_name_entry.grid(row = row_cnt, column = 1, sticky = tk.W)
        row_cnt += 1

        # Button
        button_frame = tk.Frame(self.scrollframe)
        # button_frame.pack(side = tk.BOTTOM, fill = tk.Y)
        button_frame.grid(row = row_cnt, column = 0, columnspan=2, sticky = tk.W)
        row_cnt += 1

        self.view_btn = tk.Button(button_frame, text = 'Close', command=self.on_tabClose)
        self.view_btn.pack(side=tk.RIGHT)

        self.__setState('disabled')

    def __setState(self, state):
        self.task_name_entry['state'] = state
        self.project_name_entry['state'] = state

    def update(self):
        self.__setState('normal')
        self.ui_task_name.set(self.task_ins.name)
        self.__setState('disabled')
        # self.ui_task_name.set(self.task_ins.name)

    def setInstance(self, task_ins):
        self.task_ins = task_ins
        self.update()
        ## Event Setup
        #############################3
    def on_tabClose(self):
        # self.forget()
        self.container.forget(self)
