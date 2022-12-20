import tkinter as tk
import re
# from setting.settingmanager import *
from core.eventhandler import *

class FunctionBar(tk.Frame):
    def __init__(self, event_handler, *args, **kwargs):
        super(FunctionBar, self).__init__(*args, **kwargs)

        self.event_handler = event_handler
        # self.event_handler.registEvent(Event.Record, self.rev_Record, EventHandler.OnAction)

        ## Gui Setup
        #############################3
        self.new_button = self.addFunctionBtn('New Task')
        self.new_button.pack(side = tk.LEFT, padx = 1, pady = 1)

        self.new_button = self.addFunctionBtn('New Project')
        self.new_button.pack(side = tk.LEFT, padx = 1, pady = 1)

        # self.lock_button = tk.Button(self, text = 'Lock', command = self.on_termlock, borderwidth=0, anchor=tk.CENTER, background="light gray", width=6)
        # self.lock_button.pack(side = tk.LEFT, padx = 1, pady = 1)
        # self.lock_button.bind("<Enter>", lambda event: (self.on_buttonEnter(event, ignore_txt='Unlock')))
        # self.lock_button.bind("<Leave>", lambda event: (self.on_buttonLeave(event, ignore_txt='Unlock')))

        # term_type = [
        #     "serial",
        #     "local",
        #     "stdio",
        #     "test"
        # ] #etc
        # self.term_type_str = tk.StringVar(self)
        # self.term_type_str.set(term_type[0]) # default value
        # term_type_menu = tk.OptionMenu(self, self.term_type_str, *term_type)
        # term_type_menu.pack(side = tk.LEFT, padx = 1, pady = 1)

        self.addSeperator()

        self.exit_button = tk.Button(self, text = 'Exit', command = lambda :self.event_handler.notify(Event.Exit, msg = 'exit'), borderwidth=0, anchor=tk.CENTER, background="light gray")
        self.exit_button.pack(side = tk.LEFT, padx = 1, pady = 1)
        self.exit_button.bind("<Enter>", self.on_buttonEnter)
        self.exit_button.bind("<Leave>", self.on_buttonLeave)

        # self.addSeperator()

        ## Event Setup
        #############################3

    def addSeperator(self):
        seperator = tk.Label(self,text="|")
        seperator.pack(side = tk.LEFT)
    def addFunctionBtn(self, text, command=None):
        tmp_button = tk.Button(self, text = text, command = command, borderwidth=0, anchor=tk.CENTER, background="light gray")
        tmp_button.bind("<Enter>", self.on_buttonEnter)
        tmp_button.bind("<Leave>", self.on_buttonLeave)
        return tmp_button
    def on_buttonEnter(self, event, ignore_txt = None, foreground = 'white', background = "#357EC7"):
        if ignore_txt is not None and event.widget['text'] == ignore_txt:
            pass
        else:
            event.widget['foreground'] = foreground
            event.widget['background'] = background
    def on_buttonLeave(self, event, ignore_txt = None, foreground = 'black', background = "light gray"):
        if ignore_txt is not None and event.widget['text'] == ignore_txt:
            pass
        else:
            event.widget['foreground'] = foreground
            event.widget['background'] = background

    # def notify_record(self):
    #     dbg_debug('Notify')
    #     if self.record_button['text'] == 'Stop':
    #         self.event_handler.notify(Event.Record, msg = {'action':'stop'})
    #     else:
    #         self.event_handler.notify(Event.Record, msg = {'action':'record', 'filename':self.record_file_str.get()})
    # def rev_Record (self, event=None):
    #     dbg_info('Record', event)
    #     if event['action'] == 'record':
    #         self.record_button['text'] = 'Stop'
    #     else:
    #         self.record_button['text'] = 'Record'
