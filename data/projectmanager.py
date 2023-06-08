from data.project import *
from data.task import *
from data.annotation import *

from data.haldb import *
from utility.debug import *

# PM will only handle all hal databse's access, and provide the api for upper layer to get data.
# All ids can't use outside data module

class ProjectManager:
    # (PID TEXT, Name CHAR(255), Description VARCHAR , StartDate date)''')
    __db = HalDB()
    def __init__(self):
        pass
    def __str__(self):
        dbg_info("PorjectManager")
    def __todo_task_id_map(self, task_id):
        task_name='test'
        return task_name
    def __date_parser(self, date_name, enable_time=True):
        if  enable_time is True:
            time_fmt="%Y-%m-%d %H:%M:%S"
        else:
            time_fmt="%Y-%m-%d"

        target_date=date_name
        if date_name == "eow":
            tmp_datetime = date.today()
            weekday_idx = (tmp_datetime.weekday() + 1) % 7 
            friday = tmp_datetime + timedelta(5 - weekday_idx)
            target_date = friday.strftime(time_fmt)
        elif date_name == "lw" or date_name == "lastfriday" :
            tmp_datetime = date.today()
            weekday_idx = (tmp_datetime.weekday() + 1) % 7 
            friday = tmp_datetime - timedelta(weekday_idx + (7 - 5))
            target_date = friday.strftime(time_fmt)
        elif date_name == "nw":
            tmp_datetime = date.today()
            weekday_idx = (tmp_datetime.weekday() + 1) % 7 
            friday = tmp_datetime - timedelta(weekday_idx + (7 - 5))
            target_date = friday.strftime(time_fmt)
        elif date_name == "today":
            tmp_datetime = date.today()
            target_date = tmp_datetime.strftime(time_fmt)
        elif date_name == "now":
            tmp_datetime = datetime.now()
            target_date = tmp_datetime.strftime(time_fmt)
        else:
            pass
        return target_date

################################################################
################################################################
####  Add Function
################################################################
################################################################
    def add_project(self, name, description, start_date=None):
        new_proj=Project()
        new_proj.name=name
        new_proj.description=description
        new_proj.startDate=self.__date_parser('today', enable_time=False) if start_date is None else self.__date_parser(start_date, enable_time=False)

        dbg_debug('New Project:', new_proj)
        self.__db.add_project(new_proj)
    def add_task(self, proj_name, name, description, status=None, priority=None, start_date=None, due_date=None):
        proj_ins = self.__db.get_project_by_name(proj_name)
        new_task=Task()
        new_task.name=name
        new_task.description=description
        new_task.status=Status.NEW if status is None else status
        new_task.priority=Priority.MEDIUM if priority is None else priority
        new_task.startDate=self.__date_parser('today') if start_date is None else self.__date_parser(start_date)
        new_task.dueDate=self.__date_parser('today') if due_date is None else self.__date_parser(due_date)

        dbg_debug('New Task:', new_task)
        self.__db.add_task(new_task, proj_ins)
    def add_annotation(self, task_name, description):
        task_ins = self.__db.get_task_by_name(task_name)

        new_anno=Annotation()
        new_anno.description=description
        new_anno.timeStamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        dbg_debug('New Annotation:', new_anno)
        self.__db.add_annotation_by_task(new_anno, task_ins)
################################################################
################################################################
####  Get Function
################################################################
################################################################
    def get_project_by_id(self, pid):
        return self.__db.get_project_by_id(pid)
    def get_project_by_name(self, name):
        return self.__db.get_project_by_name(name)
    def get_task_by_id(self, tid):
        dbg_error('Not implement yet.')
    def get_task_by_name(self, name):
        return self.__db.get_task_by_name(name)
    def get_annotation_by_id(self, aid):
        dbg_error('Not implement yet.')

    def get_project_list(self):
        return self.__db.get_project_list()
    def get_task_list(self, proj_name = None):
        if proj_name is None:
            return self.__db.get_task_list()
        else:
            proj_ins = self.__db.get_project_by_name(proj_name)
            return self.__db.get_task_list_by_proj(proj_ins)

    def get_annotation_list(self, task_name = None):
        if task_name is None:
            return self.__db.get_annotation_list()
        else:
            task_ins = self.__db.get_task_by_name(task_name)
            return self.__db.get_annotation_list_by_task(task_ins)
################################################################
################################################################
####  update Function
################################################################
################################################################


