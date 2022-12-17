import tkinter as tk
from tkinter import ttk
import re
# from setting.settingmanager import *
from core.eventhandler import *
from gui.todotab import *
from gui.taskviewtab import *

class TabManager(ttk.Notebook):
    def __init__(self, event_handler, *args, **kwargs):
        super(TabManager, self).__init__(*args, **kwargs)

        self.event_handler = event_handler
        # self.event_handler.registEvent(Event.Record, self.rev_Record, EventHandler.OnAction)

        ## Gui Setup
        #############################3
        # create frames
        self.todo_tab = TODOTab(event_handler, self, width=400, height=280)
        self.todo_tab.pack(side = tk.TOP, fill='both', expand=True)

        # frame2 = ScrollableFrame(self, width=400, height=280)
        frame2 = ttk.Frame(self, width=400, height=280)
        frame2.pack(side = tk.TOP, fill='both', expand=True)

        frame3 = ttk.Frame(self, width=400, height=280)
        frame3.pack(side = tk.TOP, fill='both', expand=True)

        # add frames to notebook
        self.add(self.todo_tab, text='TODO List')
        self.add(frame2, text='Summary')
        self.add(frame3, text='Profile')

        self.on_openTaskView()
    def on_openTaskView(self):
        tmp_task_view = TaskViewTab(self.event_handler, self)
        self.add(tmp_task_view, text='TaskView')

        ## Event Setup
        #############################3

