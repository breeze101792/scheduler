from datetime import *
from TaskDB import *

from Project import *
from Task import *
from Annotation import *

# Hal layer only need to connect dabase, no need to do compilcated opteration

class HalDB:
    def __init__(self):
        self.task_database = TaskDB()
        self.task_database.connect()
    def __is_proj_exist(self, proj_id):
        pass
    def __is_task_exist(self, task_id):
        pass
    def __dblist_to_proj(self, dblist):
        tmp_proj = Project()
        if dblist is not None:
            tmp_proj.pid         = dblist[0]
            tmp_proj.name        = dblist[1]
            tmp_proj.description = dblist[2]
            tmp_proj.startDate   = dblist[3]
        return tmp_proj
    def __dblist_to_task(self, dblist):
        tmp_task = Task()
        if dblist is not None:
            tmp_task.tid         = dblist[0]
            tmp_task.pid         = dblist[1]
            tmp_task.name        = dblist[2]
            tmp_task.description = dblist[3]
            tmp_task.status      = dblist[4]
            tmp_task.priority    = dblist[5]
            tmp_task.startDate   = dblist[6]
            tmp_task.dueDate     = dblist[7]
            tmp_task.endDate     = dblist[8]
        return tmp_task
    def __dblist_to_anno(self, dblist):
        # print(dblist)
        tmp_anno = Annotation()
        if dblist is not None:
            tmp_anno.aid         = dblist[0]
            tmp_anno.description = dblist[1]
            tmp_anno.pid         = dblist[2]
            tmp_anno.tid         = dblist[3]
            tmp_anno.type        = dblist[4]
            tmp_anno.timeStamp   = dblist[5]
        return tmp_anno
# Add Function
################################################################

    def add_project(self, proj_ins):
        # print(proj_ins)
        ret = self.task_database.insert_project(name=proj_ins.name, description=proj_ins.description, start_date=proj_ins.startDate)
        self.task_database.commit()

    def add_task(self, task_ins, proj_ins):
        self.task_database.insert_task(pid=proj_ins.pid, name=task_ins.name, description=task_ins.description, \
                status = task_ins.status, priority = task_ins.priority, \
                start_date = task_ins.startDate, due_date = task_ins.dueDate, end_date = task_ins.endDate)
        self.task_database.commit()
    def add_annotation_by_proj(self, anno_ins, proj_ins):
        ret = self.task_database.insert_annotation(annotation=anno_ins.annotation, pid=proj_ins.pid, time_stamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.task_database.commit()
    def add_annotation_by_task(self, anno_ins, task_ins):
        ret = self.task_database.insert_annotation(annotation=anno_ins.description, pid=task_ins.pid, tid=task_ins.tid, time_stamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.task_database.commit()

# Project
################################################################
    # def get_project_by_id(self, pid):
    #     tmp_proj_raw = self.task_database.query_project_by_id(pid)
    #     tmp_proj=self.__dblist_to_proj(tmp_proj_raw)
    #     return tmp_proj
    def get_project_by_name(self, proj_name):
        tmp_proj_raw = self.task_database.query_project_by_name(proj_name)
        tmp_proj=self.__dblist_to_proj(tmp_proj_raw)
        return tmp_proj
    def get_project_list(self):
        # return self.task_database.query_for_all_project()
        ret_projs=[]
        for each_proj in self.task_database.query_for_all_project():
            ret_projs.append(self.__dblist_to_proj(each_proj))
        return ret_projs

# Task
################################################################
    def get_task_list(self):
        task_list = []
        for each_task in self.task_database.query_for_all_task():
            tmp_task = self.__dblist_to_task(each_task)
            task_list.append(tmp_task)

        # print(task_list)
        return task_list

    # def get_task_by_id(self, tid):
    #     tmp_task_raw = self.task_database.query_task_by_id(tid)
    #     tmp_task = self.__dblist_to_task(tmp_task_raw)
    #     return tmp_task
    def get_task_by_name(self, task_name):
        tmp_task_raw = self.task_database.query_task_by_name(task_name)
        tmp_task = self.__dblist_to_task(tmp_task_raw)
        return tmp_task

    def get_task_list_by_proj(self, proj_ins, status=None, priority=None):
        task_list = []
        for each_task in self.task_database.query_task_list_by_proj_id(proj_ins.pid, status=status, priority=priority):
            tmp_task = self.__dblist_to_task(each_task)
            task_list.append(tmp_task)
        return task_list
    # def get_task_list_by_proj_id(self, pid, status=None, priority=None):
    #     return self.task_database.query_task_list_by_proj_id(pid, status=status, priority=priority)
    # def get_task_list_by_proj_name(self, proj_name, status=None, priority=None):
    #     tmp_proj = self.get_project_by_name(proj_name)
    #     return self.task_database.query_task_list_by_proj_id(tmp_proj.pid, status=status, priority=priority)
# Annotation
################################################################
    def get_annotation_list(self):
        # return self.task_database.query_for_all_annotation()
        anno_list = []
        anno_list_raw = self.task_database.query_for_all_annotation()
        for each_raw_anno in anno_list_raw:
            anno_list.append(self.__dblist_to_anno(each_raw_anno))
        return anno_list
    def get_annotation_list_by_task(self, task_ins):
        anno_list = []
        anno_list_raw = self.task_database.query_annotation_list_by_task_id(task_ins.tid)
        for each_raw_anno in anno_list_raw:
            anno_list.append(self.__dblist_to_anno(each_raw_anno))
        return anno_list
    # def get_annotation_list_by_task_name(self):
    #     return self.task_database.query_for_all_annotation()

if __name__ == '__main__':
    haldb = HalDB()

    print("## Project ")
    print("################################################################")
    tmp_proj=Project()
    tmp_proj.name="DB Project"
    tmp_proj.description="This project only for testing db"
    tmp_proj.startDate=datetime.now().strftime("%Y-%m-%d")
    haldb.add_project(tmp_proj)

    # queried_proj = haldb.get_project_by_id("P00000001")
    # print("Search by project ID", queried_proj)

    queried_proj = haldb.get_project_by_name("DB Project")
    print("Search by project name", queried_proj)

    plist = haldb.get_project_list()
    print(plist)

    print("## Task ")
    print("################################################################")
    # (TID TEXT, PID TEXT, Name CHAR(255), Description VARCHAR DEFAULT "", Status INT DEFAULT 0, Priority INT DEFAULT 0, StartDate DATETIME DEFAULT "0001-01-01", DueDate DATETIME DEFAULT "0001-01-01", EndDate DATETIME DEFAULT "0001-01-01")''')
    tmp_task = Task()
    tmp_task.name="Testing Task"
    tmp_task.pid="P00000001"
    tmp_task.description="This Task only for testing db"
    tmp_task.status=0
    tmp_task.priority=0
    tmp_task.startDate=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tmp_task.endDate=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tmp_task.dueDate=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    haldb.add_task(tmp_task, queried_proj)

    # query_task = haldb.get_task_by_id('T00000001')
    # print("Search by task id", query_task)
    search_task = haldb.get_task_by_name("Testing Task")
    print("Search by task id", search_task)

    query_task = haldb.get_task_list_by_proj(queried_proj, status=None, priority=0)
    print("Search task by proj id", query_task)

    # query_task = haldb.get_task_list_by_proj_id('P00000001', status=None, priority=0)
    # print("Search task by proj id", query_task)

    # query_task = haldb.get_task_list_by_proj_name('proj 2', status=0, priority=None)
    # print("Search task by proj name", query_task)

    tlist = haldb.get_task_list()
    print(tlist)

    print("## Annotation ")
    print("################################################################")
    tmp_anno = Annotation()
    tmp_anno.pid="P00000001"
    tmp_anno.pid="T00000001"
    tmp_anno.annotation="This Anno only for descript task"
    haldb.add_annotation_by_task(tmp_anno, search_task)

    at_list = haldb.get_annotation_list_by_task(search_task)
    print(at_list)

    alist = haldb.get_annotation_list()
    print(alist)
