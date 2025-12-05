from datetime import *

from utility.debug import *
from utility.cli import *

from Project import *
from Task import *
from Annotation import *

from ProjectManager import *
# User for some basic function including add/modify
class Operator:
    # (PID TEXT, Name CHAR(255), Description VARCHAR , StartDate date)''')
    # (TID TEXT, PID TEXT, Name CHAR(255), Description VARCHAR DEFAULT "", Status INT DEFAULT 0, Priority INT DEFAULT 0, StartDate DATETIME DEFAULT "0001-01-01", DueDate DATETIME DEFAULT "0001-01-01", EndDate DATETIME DEFAULT "0001-01-01")''')
    def __init__(self):
        self.__pm = ProjectManager()
    def __str__(self):
        print("Porject")
    def __add_proj(self, args):
        dbg_debug("Add Proj")
        arg_dict = args
        arg_key = list(arg_dict.keys())
        # dbg_debug(name=arg_dict['name'], description = arg_dict['description'], start_date=arg_dict['start'])
        if 'name' not in arg_key:
            dbg_warning('No proj name specified.')
            return False
        else:
            proj_name=arg_dict['name']

        if 'description' not in arg_key:
            dbg_warning('No proj description specified.')
            return False
        else:
            proj_desc=arg_dict['description']

        # proj_desc=arg_dict['description'] if 'description' in arg_key else None

        proj_start=arg_dict['start'] if 'start' in arg_key else None

        self.__pm.add_project(name=proj_name, description = proj_desc, start_date=proj_start)
        return True
    def __add_task(self, args):
        dbg_debug("Add Task")
    # (TID TEXT, PID TEXT, Name CHAR(255), Description VARCHAR DEFAULT "", Status INT DEFAULT 0, Priority INT DEFAULT 0, StartDate DATETIME DEFAULT "0001-01-01", DueDate DATETIME DEFAULT "0001-01-01", EndDate DATETIME DEFAULT "0001-01-01")''')
        arg_dict = args
        arg_key = list(arg_dict.keys())
        if 'project' not in arg_key:
            dbg_warning('No task project specified.')
            return False
        else:
            proj_name=arg_dict['project']

        if 'name' not in arg_key:
            dbg_warning('No task name specified.')
            return False
        else:
            task_name=arg_dict['name']

        # if 'description' not in arg_key:
        #     dbg_debug('No task description specified.')
        #     return False
        # else:
        #     task_desc=arg_dict['description']
        task_desc=arg_dict['description'] if 'description' in arg_key else None

        task_status=arg_dict['status'] if 'status' in arg_key else None
        task_priority=arg_dict['priority'] if 'priority' in arg_key else None
        task_start=arg_dict['start'] if 'start' in arg_key else None
        task_due=arg_dict['due'] if 'due' in arg_key else None

        self.__pm.add_task(proj_name=proj_name, name=task_name, description = task_desc, status=task_status, priority=task_priority, start_date=task_start, due_date=task_due)
        return True

    def __add_anno(self, args):
        # (AID TEXT, RID TEXT, Annotation CHAR(255), Type INT DEFAULT 1, TimeStamp DATETIME)''')
        arg_dict = args
        arg_key = list(arg_dict.keys())

        if 'description' in arg_key:
            anno_desc=arg_dict['description']
        # elif 'anno' in arg_key:
        #     anno_desc=arg_dict['anno']
        else:
            dbg_warning('No description specify.')
            return False

        if 'task' not in arg_key:
            dbg_warning('No task name specified.')
            return False
        else:
            task_name=arg_dict['task']

        # task_desc=arg_dict['description'] if 'description' in arg_key else None

        # print("Annotation")
        self.__pm.add_annotation(task_name=task_name, description = anno_desc)
        return True
    def add(self, args):
        func_ret=False
        # arg_dict = ArgParser.args_parser(args)
        arg_dict = args
        arg_key = list(arg_dict.keys())
        dbg_debug(arg_dict)

        if arg_dict[arg_key[1]] == "project" or arg_dict[arg_key[1]] == "proj":
            func_ret = self.__add_proj(args)
        elif arg_dict[arg_key[1]] == "annotation" or arg_dict[arg_key[1]] == "anno":
            func_ret = self.__add_anno(args)
        elif arg_dict[arg_key[1]] == "task":
            func_ret = self.__add_task(args)
        else:
            func_ret = self.__add_task(args)

        return func_ret

    def modify(self, args):
        dbg_trace(args)
        return True
    def delete(self, args):
        dbg_trace(args)
        return True

if __name__ == '__main__':
    op = Operator()
    print("## Project ")
    print("################################################################")
    op.add("add project name:test_project_name description:'desc about project' start:lw")
    print("## Task ")
    print("################################################################")
    op.add("add task project:test_project_name name:test_task_name description:'desc about task' start:today due:eow")
    print("## Annotation ")
    print("################################################################")
    op.add("add anno task:test_task_name description:'desc about task'")
    # op.modify(None)
    # op.delete(None)
