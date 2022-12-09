
from utility.debug import *
class Event:
    Status = 0
    Exit = 9
    Max = 10

class EventHandler:
    Action = 0
    Message = 1

    PreAction = 0
    OnAction = 1
    PostAction = 2
    def __init__(self, event_cnt = 5):
        self.preaction_function_list = [list() for _ in range(0, event_cnt)]
        self.onaction_function_list = [list() for _ in range(0, event_cnt)]
        self.postaction_function_list = [list() for _ in range(0, event_cnt)]
    def notify(self, event, msg=None):
        # FIXME, mixed up UI thread and data thread may cause issue.
        dbg_info('Recieve Notify from ', event, ', ', msg)
        function_list = self.preaction_function_list[event]
        dbg_debug('Pre Action: ', function_list)
        for each_fun in function_list:
            dbg_debug('Pre Action: ', each_fun)
            each_fun(msg)

        function_list = self.onaction_function_list[event]
        dbg_debug('On Action: ', function_list)
        for each_fun in function_list:
            dbg_debug('On Action: ', each_fun)
            if each_fun(msg) is False:
                dbg_error('Stop action, due to running fail at ', each_fun)
                return False

        function_list = self.postaction_function_list[event]
        dbg_debug('Post Action: ', function_list)
        for each_fun in function_list:
            dbg_debug('Post Action: ', each_fun)
            each_fun(msg)
    def registEvent(self, event, funptr, notify_type = OnAction):
        dbg_debug("Register event: {}/{} func:{} ".format(event, notify_type, funptr))
        match notify_type:
            case EventHandler.PreAction:
                self.preaction_function_list[event].append(funptr)
            case EventHandler.OnAction:
                self.onaction_function_list[event].append(funptr)
            case EventHandler.PostAction:
                self.postaction_function_list[event].append(funptr)
            case _:
                dbg_error("known Action")
