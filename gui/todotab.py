import tkinter as tk
from tkinter import ttk
import re
# from setting.settingmanager import *
from core.eventhandler import *
from xtk.scrollframe import *
from gui.tasktab import *
from gui.tab import *

class TODOTab(tk.Frame, Tab):
    def __init__(self, event_handler, project_manager, *args, **kwargs):
        super(TODOTab, self).__init__(*args, **kwargs)

        ## Vars Setup
        #############################3
        self.event_handler = event_handler
        # self.event_handler.registEvent(Event.Record, self.rev_Record, EventHandler.OnAction)
        self.project_manager = project_manager

        ## Self configs
        #############################3
        # self['background'] = 'dark gray'

        ## Gui Setup
        #############################3
        # Create the VerticalScrolledFrame
        vs_frame = VerticalScrolledFrame(self)
        vs_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)
        self.scrollframe = vs_frame.interior

        # Fake data
        self.update()

        ## Event Setup
        #############################3
    def update(self):
        # reset todo list
        for each_task in self.scrollframe.winfo_children():
            each_task.pack_forget()
            each_task.destroy()

        # add task list
        task_list = self.project_manager.get_task_list()
        dbg_debug('Task List:', task_list)
        for each_task in task_list:
            tmp_task = TaskSummaryInfo(self.event_handler, self.project_manager, self.scrollframe)
            tmp_task.setInfo(each_task)
            # tmp_task.setInfo(name = each_task.name, priority=each_task.priority, due_day=each_task.dueDate, project=self.project_manager.get_project_by_id(each_task))
            # tmp_task.setInfo(name = each_task.name, priority=each_task.priority, due_day=each_task.dueDate)
            tmp_task.setTask(each_task)
            tmp_task.pack(fill=tk.X, expand=True, padx = 5, pady = 3)
        # for each_idx in range(0, 20):
        #     tmp_task = TaskSummaryInfo(self.scrollframe)
        #     tmp_task.setInfo(name = 'Task_'+each_idx.__str__())
        #     tmp_task.pack(fill=tk.X, expand=True, padx = 5, pady = 3)


class TaskSummaryInfo(tk.LabelFrame):
    def __init__(self, event_handler, project_manager, *args, **kwargs):
        super(TaskSummaryInfo, self).__init__(*args, **kwargs)

        ## Vars Setup
        #############################3
        self.event_handler = event_handler
        # self.event_handler.registEvent(Event.Record, self.rev_Record, EventHandler.OnAction)
        self.project_manager = project_manager
        self.task_ins = None

        ## Gui Setup
        #############################3
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

        self.view_btn = tk.Button(button_frame, text = 'View', command = self.on_viewTab)
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
    def setTask(self, task_ins):
        self.setInfo(name = task_ins.name, priority=task_ins.priority, due_day=task_ins.dueDate)
        self.task_ins = task_ins
    def on_viewTab(self):
        if self.task_ins is not None:
            self.event_handler.notify(Event.Task, Event(Event.Task, 'open',self.task_ins))
        pass
        # tmp_task_tab = TaskTab(self.event_handler, self.project_manager,self)
        # self.container.add(tmp_task_tab, text='TaskView')

