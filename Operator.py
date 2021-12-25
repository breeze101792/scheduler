from datetime import *

from utility.debug import *
from utility.cli import *

from Project import *
from Task import *
from Annotation import *

# User for some basic function including add/modify
class Operator:
    # (PID TEXT, Name CHAR(255), Description VARCHAR , StartDate date)''')
    # (TID TEXT, PID TEXT, Name CHAR(255), Description VARCHAR DEFAULT "", Status INT DEFAULT 0, Priority INT DEFAULT 0, StartDate DATETIME DEFAULT "0001-01-01", DueDate DATETIME DEFAULT "0001-01-01", EndDate DATETIME DEFAULT "0001-01-01")''')
    def __init__(self):
        pass
    def __str__(self):
        print("Porject")
    def __date_parser(self, date_name, enable_time=True):
        if  enable_time is True:
            time_fmt="%Y-%m-%d %H:%M:%S"
        else:
            time_fmt="%Y-%m-%d"

        target_date=date_name
        if date_name == "eow":
            tmp_datetime = date.today()
            weekday_idx = (tmp_datetime.weekday() + 1) % 7 
            friday = tmp_datetime + timedelta(5 - weekday_idx)
            target_date = friday.strftime(time_fmt)
        elif date_name == "lw" or date_name == "lastfriday" :
            tmp_datetime = date.today()
            weekday_idx = (tmp_datetime.weekday() + 1) % 7 
            friday = tmp_datetime - timedelta(weekday_idx + (7 - 5))
            target_date = friday.strftime(time_fmt)
        elif date_name == "nw":
            tmp_datetime = date.today()
            weekday_idx = (tmp_datetime.weekday() + 1) % 7 
            friday = tmp_datetime - timedelta(weekday_idx + (7 - 5))
            target_date = friday.strftime(time_fmt)
        elif date_name == "today":
            tmp_datetime = date.today()
            target_date = tmp_datetime.strftime(time_fmt)
        elif date_name == "now":
            tmp_datetime = datetime.now()
            target_date = tmp_datetime.strftime(time_fmt)
        else:
            pass
        return target_date
    def add(self, args):
        # dbg_trace(args)
        arg_dict = ArgParser.args_parser(args)
        arg_key = list(arg_dict.keys())
        print(arg_dict)
        if arg_dict[arg_key[1]] == "project" or arg_dict[arg_key[1]] == "proj":
            print("Project")
            new_proj=Project()
            new_proj.name=arg_dict['name']
            new_proj.description=arg_dict['description']
            new_proj.startDate=self.__date_parser(arg_dict['start'])
            print(new_proj)
        elif arg_dict[arg_key[1]] == "annotation" or arg_dict[arg_key[1]] == "anno":
            print("Annotation")
            new_anno=Annotation()
            new_anno.name=arg_dict['name']
            new_anno.description=arg_dict['description']
            new_anno.description=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(new_anno)
        else:
            print("Task")
            new_task=Task()
            new_task.name=arg_dict['name']
            new_task.description=arg_dict['description']
            new_task.startDate=self.__date_parser(arg_dict['due'])
            print(new_task)

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
    op.add("add task name:test_task_name description:'desc about task' due:eow")
    print("## Annotation ")
    print("################################################################")
    op.add("add anno name:test_task_name description:'desc about task'")
    # op.modify(None)
    # op.delete(None)
