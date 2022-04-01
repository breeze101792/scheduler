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
    def add(self, args):
        # dbg_trace(args)
        # arg_dict = ArgParser.args_parser(args)
        arg_dict = args
        arg_key = list(arg_dict.keys())
        print(arg_dict)
        if arg_dict[arg_key[1]] == "project" or arg_dict[arg_key[1]] == "proj":
            print("Project")
            self.__pm.add_project(name=arg_dict['name'], description = arg_dict['description'], start_date=arg_dict['start'])
        elif arg_dict[arg_key[1]] == "annotation" or arg_dict[arg_key[1]] == "anno":
            print("Annotation")
            self.__pm.add_annotation(task_name=arg_dict['task'], description = arg_dict['description'])
        else:
            print("Task")
            self.__pm.add_task(proj_name=arg_dict['project'], name=arg_dict['name'], description = arg_dict['description'], status=0, priority=0, start_date=arg_dict['start'], due_date=arg_dict['due'])

    def modify(self, args):
        dbg_trace(args)
    def delete(self, args):
        dbg_trace(args)

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
