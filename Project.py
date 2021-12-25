# from enum import Enum, auto

class Project:
    # (PID TEXT, Name CHAR(255), Description VARCHAR , StartDate date)''')
    __pid=""
    __name=""
    __description=""
    __startDate=""

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
    def startDate(self):
        return self.__startDate
    @startDate.setter
    def startDate(self,val):
        self.__startDate = val

    def __init__(self):
        pass
    def __str__(self):
        return "Porject: %s, %s, %s, %s" % (self.__pid, self.__name, self.__description, self.__startDate)
