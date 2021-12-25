
class Annotation:
    # (AID TEXT, RID TEXT, Annotation CHAR(255), Type INT DEFAULT 1, TimeStamp DATETIME)''')
    __aid=""
    __tid=""
    __pid=""
    __annotation=""
    __timeStamp=""

    @property
    def aid(self):
        return self.__aid
    @aid.setter
    def aid(self,val):
        self.__aid = val
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
    def description(self):
        return self.__annotation
    @description.setter
    def description(self,val):
        self.__annotation = val
    @property
    def timeStamp(self):
        return self.__timeStamp
    @timeStamp.setter
    def timeStamp(self,val):
        self.__timeStamp = val

    def __init__(self):
        pass

    def __str__(self):
        return "Annotation: %s, %s, %s, %s" % (self.__tid, self.__pid,self.__annotation, self.__timeStamp)
