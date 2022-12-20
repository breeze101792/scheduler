import tkinter as tk
from tkinter import ttk
import re
# from setting.settingmanager import *
from core.eventhandler import *
from gui.todotab import *
from gui.tasktab import *

class TabManager(ttk.Notebook):
    def __init__(self, event_handler, project_manager, *args, **kwargs):
        super(TabManager, self).__init__(*args, **kwargs)

        self.event_handler = event_handler
        self.event_handler.registEvent(Event.Task, self.rev_taskEvent, EventHandler.OnAction)
        self.event_handler.registEvent(Event.GUI, self.rev_update, EventHandler.OnAction)
        self.project_manager = project_manager

        ## Gui Setup
        #############################3
        # todo frames
        self.todo_tab = TODOTab(self.event_handler, self.project_manager,self)
        self.todo_tab.pack(side = tk.TOP, fill='both', expand=True)

        # summary_tab = ScrollableFrame(self)
        summary_tab = ttk.Frame(self)
        summary_tab.pack(side = tk.TOP, fill='both', expand=True)

        # profile
        # profile_tab = ttk.Frame(self)
        # profile_tab.pack(side = tk.TOP, fill='both', expand=True)

        # add frames to notebook
        self.add(self.todo_tab, text='TODO List')
        self.add(summary_tab, text='Summary')
        # self.add(profile_tab, text='Profile')

        # self.openTaskView()
    def openTaskView(self, task = None):
        tmp_task_tab = TaskTab(self.event_handler, self.project_manager,self)
        self.add(tmp_task_tab, text='TaskView')
    def update(self):
        self.todo_tab.update()

    ## Event Setup
    #############################3
    def rev_update(self, event):
        if event.action == 'update':
            self.todo_tab.update()

    def rev_taskEvent(self, event=None):
        dbg_info('Recieve callback: ', event)

        if event.action == 'open':
            self.openTaskView(event.content)
            # self.record_button['text'] = 'Stop'
        else:
            dbg_info('Not impl event yet.')
            # self.record_button['text'] = 'Record'


