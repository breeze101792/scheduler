from time import gmtime, strftime
import threading

class DebugLevel:
    CRITICAL    = 0x1
    ERROR       = 0x2
    WARNING     = 0x4
    INFOMATION  = 0x8
    DEBUG       = 0x10
    TRACE       = 0x10
    MAX         = 0xff

class RetValue:
    ERROR = -1
    SUCCESS = 0

# test funcion could sync all ins
class Test(object):

    _i = 3

    @property
    def i(self):
        return type(self)._i

    @i.setter
    def i(self,val):
        type(self)._i = val

# TODO REMOVE this var
debug_level = DebugLevel.CRITICAL | DebugLevel.ERROR | DebugLevel.INFOMATION
debug_level = DebugLevel.MAX
def dbg_trace(*args):
    if debug_level & DebugLevel.TRACE > 0:
        dbgprint("[Trace]", *args)
def dbg_debug(*args):
    if debug_level & DebugLevel.DEBUG > 0:
        dbgprint("[Debug]", *args)
def dbg_info(*args):
    if debug_level & DebugLevel.INFOMATION > 0:
        dbgprint("[Info]", *args)
def dbg_warning(*args):
    if debug_level & DebugLevel.WARNING > 0:
        dbgprint("[Warnning]", *args)
def dbg_error(*args):
    if debug_level & DebugLevel.ERROR > 0:
        dbgprint("[Error]", *args)
def dbg_critical(*args):
    if debug_level & DebugLevel.CRITICAL > 0:
        dbgprint("[Critical]", *args)

def dbgprint(*args):
    timestamp = strftime("%d-%H:%M", gmtime())
    print("[{}]".format(timestamp) + "".join(map(str,args)))
