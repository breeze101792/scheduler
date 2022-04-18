from utility.debug import *
from utility.cli import CommandLineInterface as cli

from ProjectManager import *

from utility.debug import *

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
        return True
    def info(self, args):
        dbg_trace(args)
        return True
    def __list_proj(self, args):
        arg_dict = args
        arg_key = list(arg_dict.keys())
        # add proj name:test due:eod
        cli.print("List Project")
        project_list = self.__pm.get_project_list()
        for each_project in project_list:
            cli.print(each_project)
        return True
    def __list_task(self, args):
        arg_dict = args
        arg_key = list(arg_dict.keys())
        # add proj name:test due:eod
        cli.print("List Task")
        task_list = self.__pm.get_task_list()
        for each_task in task_list:
            cli.print(each_task)
        return True
    def __list_anno(self, args):
        arg_dict = args
        arg_key = list(arg_dict.keys())

        cli.print("List Anno")

        if 'task' not in arg_key:
            dbg_warning('No task name specified.')
            return False
        else:
            task_name=arg_dict['task']

        anno_list = self.__pm.get_annotation_list(task_name)
        for each_anno in anno_list:
            cli.print(each_anno)

        return True
    def list(self, args):
        func_ret = False
        # dbg_trace(args)
        # arg_dict = ArgParser.args_parser(args)
        arg_dict = args
        arg_key = list(arg_dict.keys())
        if len(arg_dict) > 1:
            if (arg_dict[arg_key[1]] == "project" or arg_dict[arg_key[1]] == "proj"):
                func_ret = self.__list_proj(args)
            elif arg_dict[arg_key[1]] == "task":
                func_ret = self.__list_task(args)
            elif (arg_dict[arg_key[1]] == "annotation" or arg_dict[arg_key[1]] == "anno"):
                func_ret = self.__list_anno(args)
        else:
            # dbg_debug("List Default: Task")
            func_ret = self.__list_task(args)
        return func_ret
if __name__ == '__main__':
    rp = Reporter()
    print("## Project ")
    rp.list(['list', 'project=test'])
    print("## Task ")
    rp.list(['list', 'task=test'])
