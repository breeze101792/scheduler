import tkinter as tk
from tkinter import ttk
from core.eventhandler import *
# from setting.settingmanager import *

from data.project import *
from data.task import *
from data.annotation import *
from data.projectmanager import *

class NewProjectFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        super(NewProjectFrame, self).__init__(*args, **kwargs)

        ## UI Setup
        #################################
        main_frame = tk.Frame(self, borderwidth=0) 
        main_frame.config(highlightbackground='black')
        main_frame.pack(side = "top", fill='both', expand = True)

        # main_frame.rowconfigure(0, weight=1)
        # main_frame.columnconfigure(0, weight=1)

        row_cnt = 0

        self.name_label = tk.Label(main_frame,text='Name:')
        self.name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_name = tk.StringVar(value = '[Project Name]')
        self.name_entry = tk.Entry(main_frame,textvariable=self.ui_name)
        self.name_entry.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.W)
        row_cnt += 1

        self.description_label = tk.Label(main_frame,text='Description:')
        self.description_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_description = tk.StringVar(value = '[Project Description]')
        self.description_entry = tk.Entry(main_frame,textvariable=self.ui_description)
        self.description_entry.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.W)

    @property
    def name(self):
        return self.ui_name.get()
    @property
    def description(self):
        return self.ui_description.get()

class NewTaskFrame(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        super(NewTaskFrame, self).__init__(*args, **kwargs)

        self.project_manager = ProjectManager()

        ## UI Setup
        #################################
        main_frame = tk.Frame(self, borderwidth=0) 
        main_frame.config(highlightbackground='black')
        main_frame.pack(side = "top", fill='both', expand = True)

        # main_frame.rowconfigure(0, weight=1)
        # main_frame.columnconfigure(0, weight=1)

        row_cnt = 0

        self.prjoect_name_label = tk.Label(main_frame,text='Project:')
        self.prjoect_name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_project = tk.StringVar(value = 'Task')

        project_combox = ttk.Combobox(main_frame, width = 17, textvariable=self.ui_project)
        project_list = [ x.name for x in self.project_manager.get_project_list() ]
        project_combox["values"] = project_list
        project_combox.set(project_list[0])

        # project_combox["state"] = "readonly"
        project_combox.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.W, padx=5)

        row_cnt += 1

        self.name_label = tk.Label(main_frame,text='Name')
        self.name_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_name = tk.StringVar(value = '[Task Name]')
        self.name_entry = tk.Entry(main_frame,textvariable=self.ui_name)
        self.name_entry.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.W)

        row_cnt += 1

        self.description_label = tk.Label(main_frame,text='Description:')
        self.description_label.grid(row = row_cnt, column = 0, columnspan=1, sticky = tk.W)

        self.ui_description = tk.StringVar(value = '[Task Description]')
        self.description_entry = tk.Entry(main_frame,textvariable=self.ui_description)
        self.description_entry.grid(row = row_cnt, column = 1, columnspan=1, sticky = tk.W)

        # row_cnt += 1
    @property
    def project(self):
        return self.ui_project.get()
    @property
    def name(self):
        return self.ui_name.get()
    @property
    def description(self):
        return self.ui_description.get()
class AddWin(tk.Toplevel):
    def __init__(self, event_handler, *args, **kwargs):
        super(AddWin, self).__init__(*args, **kwargs)

        self.title('Add New Project')
        self.protocol("WM_DELETE_WINDOW", self.closeWindow)

        ## Vars frame
        #################################
        self.event_handler = event_handler
        self.event_handler.registEvent(Event.Project, self.rev_Project, EventHandler.OnAction)
        self.event_handler.registEvent(Event.Task, self.rev_Task, EventHandler.OnAction)

        self.project_manager = ProjectManager()

        ## Side column frame
        #################################
        # sidebar_frame = tk.Frame(self, borderwidth=1) 
        main_frame = tk.Frame(self, borderwidth=0) 
        main_frame.config(highlightbackground='black')
        main_frame.pack(side = "top", fill='x', padx=5, pady=5)
        # main_frame.rowconfigure(0, weight=1)
        # main_frame.columnconfigure(0, weight=1)

        row_cnt = 0
        col_cnt = 0

        self.select_type_label = tk.Label(main_frame,text='Type')
        self.select_type_label.grid(row = row_cnt, column = col_cnt, columnspan=1, sticky = tk.W, padx=5)
        col_cnt += 1

        self.ui_type = tk.StringVar(value = 'Task')
        self.ui_type.trace("w", lambda name, index, mode : self.on_typeChange())
        select_type_combox = ttk.Combobox(main_frame, width = 17, textvariable=self.ui_type)
        select_type_combox["values"] = ('Task', 'Project')
        # select_type_combox["state"] = "readonly"
        select_type_combox.grid(row = row_cnt, column = col_cnt, columnspan=1, sticky = tk.W, padx=5)
        col_cnt += 1

        self.add_button = tk.Button(main_frame,text='Add', command = self.on_add)
        self.add_button.grid(row = row_cnt, column = col_cnt, columnspan=1, sticky = tk.W, padx=5)
        col_cnt += 1

        self.add_button = tk.Button(main_frame,text='Close', command = self.closeWindow)
        self.add_button.grid(row = row_cnt, column = col_cnt, columnspan=1, sticky = tk.W, padx=5)
        col_cnt += 1


        # add containter
        self.container_frame = tk.Frame(self, borderwidth=0) 
        # self.container_frame.grid(row = row_cnt, column = 0, columnspan=2, sticky = 'news', padx=5, pady=5)
        self.container_frame.pack(side = "top", fill='both', expand = True, padx=5, pady=5)
        # New Project
        self.new_project_frame = NewProjectFrame(self.container_frame)
        self.new_task_frame = NewTaskFrame(self.container_frame)

        # self.new_task_frame.grid(row = row_cnt, column = 1, columnspan=2, sticky = 'news')
        self.new_task_frame.pack(side = "top", fill='both', expand = True)

        self.withdraw()
    def on_typeChange(self):
        if self.ui_type.get() == 'Task':
            self.new_project_frame.pack_forget()
            self.new_task_frame.pack(side = "top", fill='both', expand = True)
        elif self.ui_type.get() == 'Project':
            self.new_task_frame.pack_forget()
            self.new_project_frame.pack(side = "top", fill='both', expand = True)

    def on_add(self):
        if self.ui_type.get() == 'Task':
            # self.project_manager.add_task(self, proj_name, name, description, status=None, priority=None, start_date=None, due_date=None)
            self.project_manager.add_task(proj_name = self.new_task_frame.project, name = self.new_task_frame.name, description=self.new_task_frame.description)
            # def add_task(self, proj_name, name, description, status=None, priority=None, start_date=None, due_date=None):
        elif self.ui_type.get() == 'Project':
            self.project_manager.add_project(name = self.new_project_frame.name, description = self.new_project_frame.description)

        self.event_handler.notify(Event.GUI, Event(Event.GUI, action = 'update'))
        self.withdraw()
    def rev_Project(self, msg):
        dbg_debug(msg)
        if msg.action == 'new':
            self.ui_type.set('Project')
            self.openWindow()
    def rev_Task(self, msg):
        dbg_debug(msg)
        if msg.action == 'new':
            self.ui_type.set('Task')
            self.openWindow()
    def openWindow(self):
        self.deiconify()
    def closeWindow(self):
        self.withdraw()
    def quit(self):
        self.withdraw()
