
from enum import Enum, auto

class Status(Enum):
    NEW      = auto()
    ONGOING  = auto()
    DELETE   = auto()
    WAITING  = auto()
    PENDING  = auto()
    COMPLETE = auto()
    MAX      = auto()
class Priority(Enum):
    LOW    = auto()
    MEDIUM = auto()
    HIGHT  = auto()
    MAX    = auto()

class Task:
    # (TID TEXT, PID TEXT, Name CHAR(255), Description VARCHAR DEFAULT "", Status INT DEFAULT 0, Priority INT DEFAULT 0, StartDate DATETIME DEFAULT "0001-01-01", DueDate DATETIME DEFAULT "0001-01-01", EndDate DATETIME DEFAULT "0001-01-01")''')
    __tid=""
    __pid=""
    __name=""
    __description=""
    __status=0
    __priority=0
    __startDate=""
    __dueDate=""
    __endDate=""

    @property
    def tid(self):
        return self.__tid
    @tid.setter
    def tid(self,val):
        self.__tid = val
    @property
    def pid(self):
        return self.__pid
    @pid.setter
    def pid(self,val):
        self.__pid = val
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,val):
        self.__name = val
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self,val):
        self.__description = val
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,val):
        self.__status = val
    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self,val):
        self.__priority = val
    @property
    def startDate(self):
        return self.__startDate
    @startDate.setter
    def startDate(self,val):
        self.__startDate = val
    @property
    def dueDate(self):
        return self.__dueDate
    @dueDate.setter
    def dueDate(self,val):
        self.__dueDate = val
    @property
    def endDate(self):
        return self.__endDate
    @endDate.setter
    def endDate(self,val):
        self.__endDate = val

    def __init__(self):
        pass

    def __str__(self):
        return "Task: %s, %s, %s, %s, %d, %d, %s, %s, %s" % (self.__tid, self.__pid,self.__name,self.__description,self.__status,self.__priority,self.__startDate,self.__dueDate,self.__endDate)
