from utility.debug import *


# User for some basic function including add/modify

class Reporter:
    # (PID TEXT, Name CHAR(255), Description VARCHAR , StartDate date)''')
    def __init__(self):
        pass
    def __str__(self):
        print("Reporter")
    def weekly(self, args):
        dbg_trace(args)
    def info(self, args):
        dbg_trace(args)
    def list(self, args):
        dbg_trace(args)
if __name__ == '__main__':
    rp = Reporter()
