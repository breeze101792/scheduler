from Project import *
from Task import *
from Annotation import *
from HalDB import *

# PM will only handle all hal databse's access, and provide the api for upper layer to get data.

class ProjectManager:
    # (PID TEXT, Name CHAR(255), Description VARCHAR , StartDate date)''')
    def __init__(self):
        self.__db = HalDB()
    def __str__(self):
        print("PorjectManager")
