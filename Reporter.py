from utility.debug import *
from utility.cli import *

from ProjectManager import *


# User for some basic function including add/modify

class Reporter:
    # (PID TEXT, Name CHAR(255), Description VARCHAR , StartDate date)''')
    def __init__(self):
        self.__pm = ProjectManager()
        pass
    def __str__(self):
        print("Reporter")
    def weekly(self, args):
        dbg_trace(args)
    def info(self, args):
        dbg_trace(args)
    def list(self, args):
        # dbg_trace(args)
        arg_dict = ArgParser.args_parser(args)
        arg_key = list(arg_dict.keys())
        if arg_dict[arg_key[1]] == "project" or arg_dict[arg_key[1]] == "proj":
            # add proj name:test due:eod
            print("Project")
            project_list = self.__pm.get_project_list()
            for each_project in project_list:
                print(each_project)
            # self.__pm.
        # elif arg_dict[arg_key[1]] == "task":
        #     print("Task")
        #     self.__pm.get_task_list()
        else:
            print("Task")
            task_list = self.__pm.get_task_list()
            for each_task in task_list:
                print(each_task)
if __name__ == '__main__':
    rp = Reporter()
    print("## Project ")
    rp.list('list project')
    print("## Task ")
    rp.list('list task')
