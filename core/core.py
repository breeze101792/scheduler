from gui.uimain import UIMain
import threading
from multiprocessing import Process, Pipe, current_process, Queue
import time

from utility.debug import *

class ChildProcess(Process):
    def __init__(self, *args, **kwargs):
        self.child_conn = kwargs.pop('child_conn', None)
        self.in_queue = kwargs.pop('in_queue')
        self.out_queue = kwargs.pop('out_queue')
        super().__init__(*args, **kwargs)

        ## Threading
        self.task_running = False
        self.task_thread = None

    def task(self):
        self.task_running = True
        p = current_process()

        while self.task_running is True:
            time.sleep(1)
            dbg_info("process task -> [%s] %s" % (p.pid, p.name))
    def quit(self):
        self.task_running = False
        if self.task_thread is not None:
            self.task_thread.join()

    def run(self):
        p = current_process()
        dbg_info("New process -> [%s] %s" % (p.pid, p.name))

        # self.task_thread = threading.Thread(target=self.task)
        # self.task_thread.start()

        while True:
            try:
                job = self.child_conn.recv()
            except EOFError:
                continue
            if job is None:
                dbg_debug("[%s] %s got None" % (p.pid, p.name))
                self.quit()
                break
            dbg_info("[{}] {} got a job {}".format (p.pid, p.name, job))
        dbg_info("[%s] %s terminated" % (p.pid, p.name))

class Core:
    def __init__(self):
        self.uimain = UIMain()

        self.parent_p = current_process()
        dbg_info("main process -> [%s] %s" % (self.parent_p.pid, self.parent_p.name))

        # Process Setting
        # self.processes = []
        # self.processes_n = 3

        # self.parent_conn, child_conn = Pipe()
        # in_queue = Queue()
        # out_queue = Queue()

        # child_p = ChildProcess(child_conn=child_conn, in_queue=in_queue, out_queue=out_queue, name='DataProcess')
        # child_p.start()
        # self.processes.append((self.parent_conn, child_conn, in_queue, out_queue, child_p))
    def start(self):
        # start_message = {'action':1, 'message':'UI Start'}
        # self.parent_conn.send(start_message)
        self.uimain.start()
    def quit(self):
        # self.parent_conn.send(None)
        self.uimain.quit()

