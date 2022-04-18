from time import gmtime, strftime
# import threading
import inspect
import os

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    CRITICAL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class DebugLevel:
    DISABLE    = 0x0
    CRITICAL   = 0x1
    ERROR      = 0x2
    WARNING    = 0x4
    INFOMATION = 0x8
    DEBUG      = 0x10
    TRACE      = 0x10
    MAX        = 0xff

class RetValue:
    ERROR = -1
    SUCCESS = 0

# test funcion could sync all ins
class DebugSetting(object):

    debug_level = DebugLevel.CRITICAL | DebugLevel.ERROR | DebugLevel.INFOMATION

    # @property
    # def debug_level(self):
    #     print('get debug_level')
    #     return type(self)._debug_level

    # @debug_level.setter
    # def debug_level(self,val):
    #     print('set debug_level')
    #     type(self)._debug_level = val
# print(DebugSetting._debug_level)
# DebugSetting.debug_level = DebugLevel.CRITICAL | DebugLevel.ERROR | DebugLevel.INFOMATION
# TODO REMOVE this var
# DebugSetting.debug_level = DebugLevel.CRITICAL | DebugLevel.ERROR | DebugLevel.INFOMATION
# DebugSetting.debug_level = DebugLevel.MAX
def dbg_trace(*args):
    if DebugSetting.debug_level & DebugLevel.DEBUG > 0:
        dbgprint(Bcolors.ENDC, "[Trace] ", *args, Bcolors.ENDC)
def dbg_debug(*args):
    if DebugSetting.debug_level & DebugLevel.DEBUG > 0:
        dbgprint(Bcolors.ENDC, "[Debug] ", *args, Bcolors.ENDC)
def dbg_info(*args):
    if DebugSetting.debug_level & DebugLevel.INFOMATION > 0:
        dbgprint(Bcolors.OKGREEN, "[Info] ", *args, Bcolors.ENDC)
def dbg_warning(*args):
    if DebugSetting.debug_level & DebugLevel.WARNING > 0:
        dbgprint(Bcolors.WARNING, "[Warnning] ", *args, Bcolors.ENDC)
def dbg_error(*args):
    if DebugSetting.debug_level & DebugLevel.ERROR > 0:
        dbgprint(Bcolors.ERROR, "[Error] ", *args, Bcolors.ENDC)
def dbg_critical(*args):
    if DebugSetting.debug_level & DebugLevel.CRITICAL > 0:
        dbgprint(Bcolors.BOLD, Bcolors.CRITICAL, "[Critical] ", *args, Bcolors.ENDC)

def dbgprint(*args):
    timestamp = strftime("%d-%H:%M", gmtime())
    caller_frame = inspect.stack()[2]

    caller_filename = os.path.splitext(os.path.basename(caller_frame.filename))[0]
    caller_function = caller_frame.function

    # print("[{}]".format(timestamp) + "".join(map(str,args)))
    print("[{}][{}][{}]".format(timestamp, caller_filename, caller_function) + "".join(map(str,args)))
def dbg_show():
    dbg_trace('trace')
    dbg_debug('debug')
    dbg_info('info')
    dbg_warning('warning')
    dbg_error('error')
    dbg_critical('critical')

