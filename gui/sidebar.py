import tkinter as tk
import re
# from setting.settingmanager import *
from core.eventhandler import *

class SideBar(tk.Frame):
    def __init__(self, event_handler, *args, **kwargs):
        super(SideBar, self).__init__(*args, **kwargs)

        self.event_handler = event_handler
        # self.event_handler.registEvent(Event.Record, self.rev_Record, EventHandler.OnAction)

        ## Gui Setup
        #############################3
        self.summary_frame = tk.LabelFrame(self, text = 'Summary')
        self.summary_frame.pack(side = 'top', fill=tk.BOTH, expand=True)

        self.test = tk.Label(self.summary_frame, text='TODO Task: 12')
        self.test.pack(side = 'top', fill=None, expand=False)

        ## Event Setup
        #############################3

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
