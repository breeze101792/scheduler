from utility.debug import *
class Event:
    Task = 0
    Status = 1
    Exit = 9
    Max = 10
    def __init__(self, event, action, content = None):
        self.event = event
        self.action = action
        self.content = content

    @property
    def event(self):
        return self._event
    @event.setter
    def event(self,val):
        self._event = val
        return True
    @property
    def action(self):
        return self._action
    @action.setter
    def action(self,val):
        self._action = val
        return True
    @property
    def content(self):
        return self._content
    @content.setter
    def content(self,val):
        self._content = val
        return True
    def __int__(self):
        return self.event

class EventHandler:
    Action = 0
    Message = 1
    PreAction = 0
    OnAction = 1
    PostAction = 2
    def __init__(self, event_cnt = 10):
        self.preaction_function_list = [list() for _ in range(0, event_cnt)]
        self.onaction_function_list = [list() for _ in range(0, event_cnt)]
        self.postaction_function_list = [list() for _ in range(0, event_cnt)]
    def notify(self, event, msg=None):
        # FIXME, mixed up UI thread and data thread may cause issue.
        dbg_info('Recieve Notify from ', int(event), ', ', msg)
        function_list = self.preaction_function_list[int(event)]
        dbg_debug('Pre Action: ', function_list)
        for each_fun in function_list:
            dbg_debug('Pre Action: ', each_fun)
            each_fun(msg)

        function_list = self.onaction_function_list[int(event)]
        dbg_debug('On Action: ', function_list)
        for each_fun in function_list:
            dbg_debug('On Action: ', each_fun)
            if each_fun(msg) is False:
                dbg_error('Stop action, due to running fail at ', each_fun)
                return False

        function_list = self.postaction_function_list[int(event)]
        dbg_debug('Post Action: ', function_list)
        for each_fun in function_list:
            dbg_debug('Post Action: ', each_fun)
            each_fun(msg)
    def registEvent(self, event, funptr, notify_type = OnAction):
        dbg_debug("Register event: {}/{} func:{} ".format(int(event), notify_type, funptr))
        match notify_type:
            case EventHandler.PreAction:
                self.preaction_function_list[int(event)].append(funptr)
            case EventHandler.OnAction:
                self.onaction_function_list[int(event)].append(funptr)
            case EventHandler.PostAction:
                self.postaction_function_list[int(event)].append(funptr)
            case _:
                dbg_error("known Action")

    ## Sampel function
    ################################################################
    # def notify_callback(self):
    #     dbg_debug('Notify')

    #     if self.record_button['text'] == 'Stop':
    #         self.event_handler.notify(Event.Record, msg = {'action':'stop'})
    #     else:
    #         self.event_handler.notify(Event.Record, msg = {'action':'record', 'filename':self.record_file_str.get()})
    # def rev_callback (self, event=None):
    #     dbg_info('Recieve callback: ', event)

    #     if event['action'] == 'record':
    #         self.record_button['text'] = 'Stop'
    #     else:
    #         self.record_button['text'] = 'Record'
