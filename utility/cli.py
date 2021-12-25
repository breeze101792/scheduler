from enum import Enum, auto
import threading
import time
import subprocess as sp
import codecs
import re

from .debug import *
from .utils import getch

class EUIMode(Enum):
    WORD = auto()
    INTERCTIVE = auto()
    FILE = auto()
    LIST = auto()
    MAX = auto()


class ArgParser:
    @staticmethod
    def args_parser(args):
        def_key_prefix='arg_'
        def_key_idx=0
        dbg_trace(args)
        arg_dict=dict()
        pattern = re.compile(r'''((?:[^\s"']|"[^"]*"|'[^']*')+)''')
        for each_arg in pattern.split(args):
            if each_arg == '' or each_arg == " ":
                continue
            tmp_list=each_arg.split(":")

            if len(tmp_list) == 2:
                arg_dict[tmp_list[0]] = tmp_list[1]
            elif len(tmp_list) == 1:
                arg_dict[def_key_prefix+def_key_idx.__str__()] = tmp_list[0]
                def_key_idx=def_key_idx+1
        # print(arg_dict)
        return arg_dict

class CommandLineInterface:
    def __init__(self):
        #### control vars ###
        self.__flag_running = True
        self.__promote="cli> "

        ### local vars ###
        self.__mode = EUIMode.FILE
        self.__history_list = ['history','help', 'exit']
        self.__function_dict=dict()

        ### Function Configs ###
        self.regist_cmd("help", self.__help, "Print help")
        self.regist_cmd("exit", self.__exit, "Exit the program")
        self.regist_cmd("history", self.__hist, "Print history")
    def __exit(self, args):
        self.ui_print_line("Exit program")
        exit()
    def __hist(self, args):
        self.ui_print_line("History")
        # for each_cmd in self.__history_list:
        #     self.ui_print_line(" " + each_cmd)
        for each_idx in range(0, len(self.__history_list)):
            self.ui_print_line("% 4d. %s" % (each_idx,  self.__history_list[each_idx]))

    def __help(self, args):
        self.ui_print_line("Help")
        # print("   under construction")
        for each_key in self.__function_dict.keys():
            self.ui_print_line("  %- 8s: %s" % (each_key, self.__function_dict[each_key][1]))
    def set_mode(self, mode):
        self.__mode = mode

    @staticmethod
    def ui_print(*args):
        print("".join(map(str,args)), end="", flush=True)
    @staticmethod
    def ui_print_line(*args):
        print("".join(map(str,args)), flush=True)
    def __print_line_buffer(self, line_buffer, cursor_shift_idx):
        trailing_space_nmu=16
        # self.ui_print("\r"+" "*(len(self.__promote)+len(line_buffer)))
        # self.ui_print("\r                                             ")
        self.ui_print("\r"+self.__promote+line_buffer+trailing_space_nmu*" ")
        self.ui_print("\033[%dD" % (cursor_shift_idx + trailing_space_nmu))

    def parse(self):
        pass
    def regist_cmd(self, key_word, func_ptr, description=""):
        self.__function_dict[key_word] = [func_ptr, description]
        # print(self.__function_dict)
    def run_once(self, line_args):
        line_buffer=line_args
        cmd_token = line_buffer.split()
        for each_key in self.__function_dict.keys():
            if each_key == cmd_token[0]:
                self.__function_dict[each_key][0](cmd_token)
                break
    def run(self):
        while self.__flag_running == True:
            line_buffer=self.get_line()
            self.run_once(line_buffer)

    def get_line(self):
        ckey_timestatmp=time.time()
        pkey_timestatmp=time.time()
        key_timeout=50.0

        line_buffer=""
        line_bakup_buffer=""
        esc_dectect=False
        pkey_press=""
        history_idx=0
        buffer_cusor_idx=0

        # self.ui_print(self.__promote)
        self.ui_print("\r"+self.__promote+line_buffer)
        # ui_print(self.__promote)
        while self.__flag_running == True:
            pkey_timestatmp = ckey_timestatmp
            key_press = getch()
            ckey_timestatmp=time.time()

            # print("Key Code: ", key_press.encode("ascii"))

            # special key press
            if key_press == chr(0x1b):
                # esc
                esc_dectect=True
                # dbg_debug("Esc Key")
                continue
            elif key_press == chr(0x04):
                # ctrl + d
                self.__exit(None)
            elif key_press == chr(0x03):
                # ctrl + c
                line_buffer=""
                line_bakup_buffer=""
                esc_dectect=False
                pkey_press=""
                history_idx=0
                buffer_cusor_idx=0
                self.__print_line_buffer(line_buffer, buffer_cusor_idx)
            elif key_press == chr(0x7f):
                # backspace
                # print("test")
                tmp_idx=len(line_buffer)-buffer_cusor_idx-1
                line_buffer = line_buffer[:tmp_idx] + line_buffer[tmp_idx + 1:]
                # self.ui_print_line('')
                # self.ui_print_line("Start: " + line_buffer[:tmp_idx])
                # self.ui_print_line("End: " + line_buffer[tmp_idx:] )
                self.__print_line_buffer(line_buffer, buffer_cusor_idx)
                continue
            # elif key_press.encode("ascii") == b'\x1f':

            if ckey_timestatmp - pkey_timestatmp < key_timeout and esc_dectect is True:
                if key_press == '[':
                    pkey_press = key_press
                    continue
                elif pkey_press == '[':
                    if key_press == 'D':
                        # return('left')
                        # self.ui_print_line("Cursor Idx: ",buffer_cusor_idx)
                        if len(line_buffer) > buffer_cusor_idx + 1:
                            buffer_cusor_idx=buffer_cusor_idx + 1
                            self.__print_line_buffer(line_buffer, buffer_cusor_idx)
                        # elif 1 == buffer_cusor_idx:
                        #     buffer_cusor_idx=buffer_cusor_idx + 1
                        #     self.ui_print("\r"+self.__promote+line_buffer)
                        #     self.ui_print("\033[%dD" % (buffer_cusor_idx))
                    elif key_press == 'C':
                        # return('right')
                        # self.ui_print_line("Cursor Idx: ",buffer_cusor_idx)
                        if 1 <= buffer_cusor_idx:
                            buffer_cusor_idx=buffer_cusor_idx - 1
                            self.__print_line_buffer(line_buffer, buffer_cusor_idx)
                        # elif 1 == buffer_cusor_idx:
                        #     buffer_cusor_idx=buffer_cusor_idx - 1
                        #     self.__print_line_buffer(line_buffer, buffer_cusor_idx)
                    elif key_press == 'A':
                        # self.ui_print_line("Hist Idx: ",history_idx)
                        # return('up')
                        if 0 == history_idx:
                            line_bakup_buffer = line_buffer
                        if len(self.__history_list)  > history_idx:
                            history_idx=history_idx + 1
                            buffer_cusor_idx = 0
                            line_buffer=self.__history_list[-history_idx]
                        self.__print_line_buffer(line_buffer, buffer_cusor_idx)
                    elif key_press == 'B':
                        # self.ui_print_line("Hist Idx: ",history_idx)
                        # return('down')
                        if 1 < history_idx:
                            history_idx=history_idx - 1
                            buffer_cusor_idx = 0
                            line_buffer=self.__history_list[-history_idx]
                        elif 1 == history_idx:
                            history_idx=history_idx - 1
                            line_buffer = line_bakup_buffer
                        self.__print_line_buffer(line_buffer, buffer_cusor_idx)
                esc_dectect=False
                pkey_press=''
                continue
            else:
                esc_dectect=False
                pkey_press=''

            # normal key press
            if key_press in ("\r", "\n"):
                # print("Enter")
                self.ui_print("\n")
                break
            else:
                line_buffer=line_buffer+key_press
                self.__print_line_buffer(line_buffer, buffer_cusor_idx)
                # update buffer
                continue
        self.__history_list.append(line_buffer)
        # self.ui_print_line(self.__history_list)
        return line_buffer
    # def start_thread(self):
    #     x = threading.Thread(target=self.key_press, args=(0,))
    #     x.start()
    #     self.ui_print_line("End of init key thread")

    # def key_press(self, test):
    #     while True:
    #         x_tmp = getch()
    #         self.ui_print_line("KeyPress: {}".format(x_tmp))
    #         time.sleep(0.05)
    #         if x_tmp in ("q", "Q", "x", "X"):
    #             # self.ui_print_line(psettings.get('msg_exit'))
    #             return


if __name__ == '__main__':
    debug_level=DebugLevel.MAX
    test_cli = CommandLineInterface()
    test_cli.set_mode(EUIMode.INTERCTIVE)
    test_cli.run()
