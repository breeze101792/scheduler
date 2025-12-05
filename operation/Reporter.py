from utility.debug import *
from utility.cli import CommandLineInterface as cli

from project.ProjectManager import *

from utility.debug import *
from tabulate import tabulate

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
    def __list_proj(self, args = None):
        # add proj name:test due:eod
        cli.print("List Project")
        project_list = self.__pm.get_project_list()
        if project_list:
            project_headers = ["Name", "Description", "Start Date"]
            project_data = []
            for each_project in project_list:
                project_data.append([each_project.name, each_project.description, each_project.startDate])
            cli.print(tabulate(project_data, headers=project_headers, tablefmt="fancy_grid"))
        else:
            cli.print("No projects found.")
        return True
    def __list_task(self, args = None):
        # add proj name:test due:eod
        cli.print("List Task")
        task_list = self.__pm.get_task_list()
        if task_list:
            task_headers = ["Project", "Name", "Description", "Status", "Priority", "Start Date", "Due Date", "End Date"]
            task_data = []
            for each_task in task_list:
                task_data.append([
                    self.__pm.get_project_by_id(each_task.pid).name,
                    each_task.name,
                    each_task.description,
                    Status.to_string(each_task.status),
                    Priority.to_string(each_task.priority),
                    each_task.startDate,
                    each_task.dueDate,
                    each_task.endDate
                ])
            cli.print(tabulate(task_data, headers=task_headers, tablefmt="fancy_grid"))
        else:
            cli.print("No tasks found.")
        return True
    # def __list_anno(self, args):
    #     arg_dict = args
    #     arg_key = list(arg_dict.keys())
    #
    #     cli.print("List Anno")
    #
    #     if 'task' not in arg_key:
    #         dbg_warning('No task name specified. Listing all annotations.')
    #         task_name=None
    #     else:
    #         task_name=arg_dict['task']
    #
    #     anno_list = self.__pm.get_annotation_list(task_name)
    #     if anno_list:
    #         anno_headers = ["Annotation ID", "Content", "Timestamp", "Task ID"]
    #         anno_data = []
    #         for each_anno in anno_list:
    #             anno_data.append([each_anno.aid, each_anno.content, each_anno.timestamp, each_anno.tid])
    #         cli.print(tabulate(anno_data, headers=anno_headers, tablefmt="fancy_grid"))
    #     else:
    #         cli.print("No annotations found.")
    #
    #     return True
    def __show_proj(self, proj_name):
        proj_ins = self.__pm.get_project_by_name(proj_name)
        task_list = self.__pm.get_task_list(proj_name)
        
        # Project details
        project_data = [
            ["Name", proj_ins.name],
            ["Description", proj_ins.description],
            ["Start Date", proj_ins.startDate]
        ]
        cli.print(tabulate(project_data, headers=["Attribute", "Value"], tablefmt="fancy_grid"))

        # Task list for the project
        if task_list:
            task_headers = ["Task Name", "Due Date", "Description"]
            task_data = []
            for each_task in task_list:
                task_data.append([each_task.name, each_task.dueDate, each_task.description])
            cli.print("\nTasks for Project '{}':".format(proj_name))
            cli.print(tabulate(task_data, headers=task_headers, tablefmt="fancy_grid"))
        else:
            cli.print("\nNo tasks found for Project '{}'.".format(proj_name))
        return True
    def __show_task(self, task_name):
        task_ins = self.__pm.get_task_by_name(task_name)
        anno_list = self.__pm.get_annotation_list(task_name)
        
        # Task details
        task_headers = ["Name", "Project", "Description", "Status", "Priority", "Start Date", "Due Date", "End Date"]
        task_data = [[
            task_ins.name,
            self.__pm.get_project_by_id(task_ins.pid).name,
            task_ins.description,
            Status.to_string(task_ins.status),
            Priority.to_string(task_ins.priority),
            task_ins.startDate,
            task_ins.dueDate,
            task_ins.endDate
        ]]
        cli.print(tabulate(task_data, headers=task_headers, tablefmt="fancy_grid"))

        # Annotation list for the task
        if anno_list:
            anno_headers = ["Annotation ID", "Content", "Timestamp"]
            anno_data = []
            for each_anno in anno_list:
                anno_data.append([each_anno.aid, each_anno.content, each_anno.timestamp])
            cli.print("\nAnnotations for Task '{}':".format(task_name))
            cli.print(tabulate(anno_data, headers=anno_headers, tablefmt="fancy_grid"))
        else:
            cli.print("\nNo annotations found for Task '{}'.".format(task_name))
        return True

    def show(self, args):
        func_ret = False
        # dbg_trace(args)
        # arg_dict = ArgParser.args_parser(args)
        arg_dict = args
        arg_key = list(arg_dict.keys())
        if len(arg_dict) > 1:
            if 'project' in arg_key:
                func_ret = self.__show_proj(arg_dict['project'])
            elif 'task' in arg_key:
                func_ret = self.__show_task(arg_dict['task'])
            else:
                print("Please specify project/task")
        else:
            print("Please specify project/task")

        return func_ret

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
            # elif (arg_dict[arg_key[1]] == "annotation" or arg_dict[arg_key[1]] == "anno"):
            #     func_ret = self.__list_anno(args)
            else:
                func_ret = self.__list_proj()
        else:
            # dbg_debug("List Default: Task")
            func_ret = self.__list_proj()
        return func_ret
if __name__ == '__main__':
    rp = Reporter()
    print("## Project ")
    rp.list(['list', 'project=test'])
    print("## Task ")
    rp.list(['list', 'task=test'])
