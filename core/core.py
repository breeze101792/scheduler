from utility.cli import CommandLineInterface

from core.config import AppConfigManager

from project.Project import *
from project.Task import *
from project.Annotation import *

from operation.Operator import *
from operation.Reporter import *

class SchedCLI(CommandLineInterface):
    def __init__(self, promote='sched'):
        appcgm = AppConfigManager()

        welcome_message = (
            f"HI, Wellcome to your scheduler."
        )
        super().__init__(promote, wellcome_message = welcome_message)

        # preset
        self.history_path = appcgm.get_path('log')

        # command setup
        op = Operator()

        self.regist_cmd("add", op.add, "Add project/Task/Annotation", arg_list=['project', 'task', 'annotation', 'name', 'description'])
        # self.regist_cmd("modify", op.modify, "Modify project/Task/Annotation")
        # self.regist_cmd("delete", op.delete, "Delete project/Task/Annotation")

        rp = Reporter()
        # self.regist_cmd("info", rp.info, "Show current status of working projects")
        self.regist_cmd("weekly", rp.weekly, "Show report of last week")
        self.regist_cmd("list", rp.list, "list current todo list", arg_list=['project', 'task', 'annotation'])
        self.regist_cmd("show", rp.show, "show specify task", arg_list=['project', 'task'])

        # debug
        # self.regist_cmd("echo", echo, "Echo Command")

