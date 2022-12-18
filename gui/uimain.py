import tkinter as tk
from tkinter import ttk
# from mttkinter.mttkinter import *

import serial
import threading
import sys
import traceback

from core.eventhandler import *
from gui.functionbar import *
from gui.sidebar import *
from gui.tabmanager import *
from gui.aboutwindow import *
# from core.statusbar import *
# from setting.settingmanager import *

from utility.debug import *

from data.project import *
from data.task import *
from data.annotation import *
from data.projectmanager import *


class UIMain:
    def __init__(self):
        ## vars init
        #############################3
        self.event_handler = EventHandler(Event.Max)
        self.event_handler.registEvent(Event.Exit, self.quit, EventHandler.OnAction)
        self.project_manager = ProjectManager()

        ## tk init
        #############################3
        self.window = tk.Tk()
        self.window.title("Scheduler")
        # self.window.title("Scheduler" + ' V.' + Setting.Version)
        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self.window.geometry("640x480")

        # icon = tk.PhotoImage(file="resource/icon.png")
        # self.window.iconphoto(False, icon)

        # icon = tk.PhotoImage(file="resource/icon.png")
        # self.window.iconphoto(False, icon)

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)

        # window init
        # self.setting_manager = SettingManager()
        self.about = About()

        ## Right Click Menu
        #############################3
        # self.right_click_menu = tk.Menu(self.window, tearoff = 0)
        # self.right_click_menu.add_command(label ="Copy", command = self.term_frame.terminal.textCopy)
        # self.right_click_menu.add_command(label ="Paste", command = self.term_frame.terminal.textPaste)
        # self.right_click_menu.add_command(label ="Clipboard", command = lambda : (self.term_frame.terminal.textCopy(), self.clipboard.openWindow()))
        # self.right_click_menu.add_command(label ="Rename")
        # self.right_click_menu.add_separator()
        # self.right_click_menu.add_command(label='Advance Settings', command=self.setting_manager.openWindow)
        # self.right_click_menu.add_command(label ="Close")

        ## menu
        #############################3
        # self.window = Tk()
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)

        filemenu = tk.Menu(menu, tearoff = "off")
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open...')
        # filemenu.add_command(label='Save log as ...', command=self.on_saveTerminalText)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=lambda :self.event_handler.notify(Event.Exit, msg = 'exit'))

        ## Tool, program wide function
        #############
        toolmenu = tk.Menu(menu, tearoff = "off")
        menu.add_cascade(label='Tools', menu=toolmenu)
        toolmenu.add_separator()
        toolmenu.add_command(label='Advance Settings')

        ## Help
        #############
        helpmenu = tk.Menu(menu, tearoff = "off")
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About', command=self.about.openWindow)
        menu.add_command(label='Exit', command=lambda :self.event_handler.notify(Event.Exit, msg = 'exit'))

        ## Function Bar
        #############################3
        self.function_bar = FunctionBar(self.event_handler, self.window)
        self.function_bar.grid(row = 0, column = 0, columnspan=2, sticky = tk.W)

        main_frame = tk.Frame(self.window)
        main_frame.grid(row = 1, column = 0, columnspan=2, sticky = 'news')
        ## Side Bar
        #############################3
        self.side_bar = SideBar(self.event_handler, main_frame, width=64)
        # self.side_bar.grid(row = 2, column = 1)
        self.side_bar.pack(side = tk.LEFT, fill = tk.Y, expand = False)

        # container_frame = tk.Frame(main_frame)
        # container_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        # container_frame.grid(row = 1, column = 0, columnspan=2, sticky = 'news')

        self.tab_manager = TabManager(self.event_handler, self.project_manager, main_frame)
        self.tab_manager.pack(side = tk.LEFT, fill = tk.BOTH, expand = True, pady=(10,0))
        # test_label = FunctionBar(self.event_handler, self.window, background='gray')
        # test_label.grid(row = 1, column = 0, sticky = tk.W)

        # self.lock_button = tk.Button(self.window, text = 'Lock', borderwidth=0, anchor=tk.CENTER, background="light gray", width=6)
        # self.lock_button.grid(row = 2, column = 0, sticky = tk.W)

    def refresh(self):
        try:
            pass
        except Exception as e:
            dbg_error(e)

            traceback_output = traceback.format_exc()
            dbg_error(traceback_output)
            self.window.after(30, self.refresh)

    def quit(self, event_msg=None):
        dbg_info('Quit')
        self.window.withdraw()
        # self.setting_manager.quit()
        self.about.quit()
        self.window.quit()
    def start(self):
        dbg_info('GUI Start')
        self.window.mainloop()
        dbg_info('GUI End')

    # def do_popup(self, event):
    #     dbg_debug('Event: ', event)

    #     try:
    #         self.right_click_menu.tk_popup(event.x_root, event.y_root)
    #     finally:
    #         self.right_click_menu.grab_release()

