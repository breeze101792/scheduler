#!/usr/bin/env python3
# system function
from optparse import OptionParser

from Project import *
from Task import *
from Annotation import *

from Operator import *
from Reporter import *

# from utility.debug import *
from utility.cli import *

def echo(args):
    dbg_info(args)
def main():
    parser = OptionParser(usage='Usage: Scheduler [options] ......')
    # parser.add_option("-i", "--interactive", dest="interactive",
    #         help="Start interactive mode", action="store_true")
    parser.add_option("-p", "--project", dest="project",
            help="add project", action="store")
    parser.add_option("-t", "--task", dest="task",
            help="add task", action="store")
    parser.add_option("-a", "--annotation", dest="annotation",
            help="add annotation", action="store")
    ################################################################
    # parser.add_option("-t", "--test", dest="test",
    #         help="testing function", action="store")
    parser.add_option("-d", "--debug", dest="debug",
            help="debug mode on!!", action="store_true")
    #parser.add_option("-L", "--word-level", dest="word_level",
    #                help="Setup Word Level", default=[], action="append")

    ## Parse Options
    ################################################################
    (options, args) = parser.parse_args()

    # if options.project is not None:
    #     # psettings.set('file_name', options.file_name)
    #     print("Project")
    # elif options.task is not None: 
    #     print("Task")
    # elif options.annotation is not None: 
    #     print("annotation")
    # else:
    #     print("Default action")

    # open file

    ## Run
    ################################################################
    try:
        # dbg_info("Test")
        sched_cli = CommandLineInterface()
        op = Operator()
        sched_cli.regist_cmd("add", op.add, "Add project/Task/Annotation")
        sched_cli.regist_cmd("modify", op.modify, "Modify project/Task/Annotation")
        sched_cli.regist_cmd("delete", op.delete, "Delete project/Task/Annotation")

        rp = Reporter()
        sched_cli.regist_cmd("info", rp.info, "Show current status of working projects")
        sched_cli.regist_cmd("weekly", rp.weekly, "Show report of last week")
        sched_cli.regist_cmd("list", rp.list, "list current todo list")

        # debug
        sched_cli.regist_cmd("echo", echo, "Echo Command")

        sched_cli.run()
    except (OSError, KeyboardInterrupt):
        print("Bye")
    except:
        raise
if __name__ == '__main__':
    main()
