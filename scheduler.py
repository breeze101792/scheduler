#!/usr/bin/env python3
# system function
from optparse import OptionParser

# from utility.debug import *
from utility.cli import *
from core.core import SchedCLI

def echo(args):
    CommandLineInterface.print("Echo: ", args)
    return True
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

    if options.debug is True:
        # psettings.set('file_name', options.file_name)
        DebugSetting.debug_level = DebugLevel.CRITICAL | DebugLevel.ERROR | DebugLevel.WARNING | DebugLevel.DEBUG | DebugLevel.INFOMATION
        ## debug settings
        # DebugSetting.debug_level = DebugLevel.MAX
        # DebugSetting.debug_level = DebugLevel.MAX
        # DebugSetting.dbg_show()
        # open file

    ## Run
    ################################################################
    try:
        # dbg_info("Test")
        sched_cli = SchedCLI()
        sched_cli.run()
    except (OSError, KeyboardInterrupt):
        print("Bye")
    except:
        raise
if __name__ == '__main__':
    main()
