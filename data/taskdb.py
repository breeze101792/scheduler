import sqlite3
import os
from datetime import date

class TaskDB:
    __db_lock = False
    __db_connection = None
    __cursor = None
    __db_file= None
    def __init__(self, db_file="./test.db"):
        self.__db_file = db_file
        if not os.path.isfile(self.__db_file):
            conn = sqlite3.connect(self.__db_file)
            c = conn.cursor()
            # Create table
            c.execute('''CREATE TABLE PROJECT
                         (PID TEXT, Name CHAR(255), Description VARCHAR , StartDate date)''')

            c.execute('''CREATE TABLE TASK
                         (TID TEXT, PID TEXT, Name CHAR(255), Description VARCHAR DEFAULT "", Status INT DEFAULT 0, Priority INT DEFAULT 0, StartDate DATETIME DEFAULT "0001-01-01", DueDate DATETIME DEFAULT "0001-01-01", EndDate DATETIME DEFAULT "0001-01-01")''')

            c.execute('''CREATE TABLE ANNOTATION
                         (AID TEXT, Annotation CHAR(255), PID TEXT, TID TEXT, Type INT DEFAULT 1, TimeStamp DATETIME)''')

            # datetime format
            # 0001-01-01 00:00:00.0000000

            # # Insert a row of data
            # c.execute("INSERT INTO PROJECT VALUES ('p0','test', 'dsc','2020-10-10')")
            # c.execute("INSERT INTO TASK VALUES ('t0','test', 'dsc','2020-10-10')")
            # c.execute("INSERT INTO ANNOTATION VALUES ('a0','test', 'dsc','2020-10-10')")

            # Save (commit) the changes
            conn.commit()

            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
            conn.close()
            # print('successful init')
    def __lock(self):
        if self.__db_lock == False:
            self.__db_lock = True
            return True
        else:
            return False
    def __unlock(self):
        if self.__db_lock == True:
            self.__db_lock = False
            return True
        else:
            return False
    def __is_locked(self):
        return self.__db_lock
    def connect(self):
        if self.__is_locked():
            # print("Database is locked!")
            return False
        elif self.__db_connection is None:
            self.__lock()
            self.__db_connection = sqlite3.connect(self.__db_file)
            self.__cursor = self.__db_connection.cursor()
            self.__unlock()
            return True
        else:
            # print("Database is already connected!")
            return True
    def close(self):
        if self.__db_lock:
            # print('database is locked!\n please unlocked first!')
            return False
        elif self.__db_connection is None:
            # print('there is nothing to do!')
            return True
        else:
            self.commit()
            self.__db_connection.close()
            return True
    def commit(self):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            # print('sent commit')
            self.__db_connection.commit()
            return True
    def query_for_all_project(self):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = """SELECT * FROM PROJECT;"""
            result = self.__cursor.execute(query_str)
            self.__unlock()
            return result.fetchall()
    def query_for_all_task(self):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = """SELECT * FROM TASK;"""
            result = self.__cursor.execute(query_str)
            self.__unlock()
            return result.fetchall()
    def query_for_all_annotation(self):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = """SELECT * FROM ANNOTATION;"""
            result = self.__cursor.execute(query_str)
            self.__unlock()
            return result.fetchall()
    def query_project_by_id(self, pid):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = "SELECT * FROM PROJECT WHERE PID == '%s'" % pid
            result = self.__cursor.execute(query_str)
            self.__unlock()
            return result.fetchone()
    def query_project_by_name(self, proj_name):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = "SELECT * FROM PROJECT WHERE Name == '%s'" % proj_name
            result = self.__cursor.execute(query_str)
            self.__unlock()
            return result.fetchone()
    def query_task_by_id(self, tid):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = "SELECT * FROM TASK WHERE TID == '%s'" % tid
            result = self.__cursor.execute(query_str)
            self.__unlock()
            # print(result.fetchone())
            return result.fetchone()
    def query_task_by_name(self, task_name):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = "SELECT * FROM TASK WHERE Name == '%s'" % task_name
            result = self.__cursor.execute(query_str)
            self.__unlock()
            return result.fetchone()
    def query_task_list_by_proj_id(self, pid, status=None, priority=None):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = "SELECT * FROM TASK WHERE PID == '%s'" % pid
            if status is not None:
                query_str=query_str+" AND Status == '%s'" % status
            if priority is not None:
                query_str=query_str+" AND Priority == '%s'" % priority

            result = self.__cursor.execute(query_str)
            self.__unlock()
            return result.fetchall()
    def query_annotation_list_by_task_id(self, tid):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = "SELECT * FROM ANNOTATION WHERE TID == '%s'" % tid
            result = self.__cursor.execute(query_str)
            self.__unlock()
            # print(result.fetchall())
            return result.fetchall()
    def __get_nex_proj_id(self):
        self.__lock()
        query_str = "SELECT COUNT(PID) FROM PROJECT"
        result = self.__cursor.execute(query_str)
        self.__unlock()
        proj_cnt = result.fetchall()[0][0]
        pid = 'P{message:{fill}{align}{width}}'.format(
                message=proj_cnt.__str__(),
                fill='0',
                align='>',
                width=8,
                )
        return pid
    def __get_nex_task_id(self):
        self.__lock()
        query_str = "SELECT COUNT(TID) FROM TASK"
        result = self.__cursor.execute(query_str)
        self.__unlock()
        proj_cnt = result.fetchall()[0][0]
        tid = 'T{message:{fill}{align}{width}}'.format(
                message=proj_cnt.__str__(),
                fill='0',
                align='>',
                width=8,
                )
        return tid
    def __get_nex_anno_id(self):
        self.__lock()
        query_str = "SELECT COUNT(AID) FROM ANNOTATION"
        result = self.__cursor.execute(query_str)
        self.__unlock()
        proj_cnt = result.fetchall()[0][0]
        aid = 'A{message:{fill}{align}{width}}'.format(
                message=proj_cnt.__str__(),
                fill='0',
                align='>',
                width=8,
                )
        return aid
    def __is_proj_exist(self,pid):
        query_str = "SELECT pid FROM PROJECT WHERE PID == '%s'" % pid
        # print(query_str)
        result = self.__cursor.execute(query_str).fetchone()
        # print("test", pid, result)
        if result is None:
            # word is already in the wordbank
            return False
        else:
            return True
    def __is_task_exist(self,tid):
        query_str = "SELECT TID FROM TASK WHERE TID == '%s'" % tid
        # print(query_str)
        result = self.__cursor.execute(query_str).fetchone()
        # print("test", tid, result)
        if result is None:
            # word is already in the wordbank
            return False
        else:
            return True

    def insert_project(self, name, description, start_date = None):
        # (PID UNSIGNED INT, Name CHAR(255), Description VARCHAR , StartDate date)

        query_str = "SELECT name FROM PROJECT WHERE Name == '%s'" % name
        # print(query_str)
        if self.__is_locked():
            print('db is locked')
            return False
        else:
            self.__lock()
            result = self.__cursor.execute(query_str).fetchone()
            # print(result)
            if result is not None:
                # word is already in the wordbank
                self.__unlock()
                return False
            else:
                pid = self.__get_nex_proj_id()
                if start_date is None:
                    today = date.today()
                    start_date = today.strftime("%Y-%m-%d")
                query_str = "INSERT INTO PROJECT (PID, Name, Description, StartDate) VALUES ('%s', '%s', '%s', '%s')" % (pid, name, description, start_date)
                # print(query_str)
                result = self.__cursor.execute(query_str).fetchone()
            self.__unlock()
            return result #.fetchone()

    def insert_task(self, pid, name, description, status = 0, priority = 0, start_date = None, due_date = None, end_date = None):
        # (TID TEXT, PID TEXT, Name CHAR(255), Description VARCHAR DEFAULT "", Status INT DEFAULT 0, Priority INT DEFAULT 0, StartDate DATETIME DEFAULT "0001-01-01", DueDate DATETIME DEFAULT "0001-01-01", EndDate DATETIME DEFAULT "0001-01-01")''')

        query_str = "SELECT name FROM TASK WHERE Name == '%s'" % name
        # print(query_str)
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            result = self.__cursor.execute(query_str).fetchone()
            # print(result)
            if result is not None or self.__is_proj_exist(pid) is False:
                # word is already in the wordbank
                self.__unlock()
                return False
            else:
                tid = self.__get_nex_task_id()
                if start_date is None:
                    today = date.today()
                    start_date = today.strftime("%Y-%m-%d")
                query_str = "INSERT INTO TASK (TID, PID, Name, Description, Status, Priority, StartDate, DueDate, EndDate) VALUES ('%s', '%s', '%s', '%s', %i, %i ,'%s', '%s', '%s')" % (tid, pid, name, description, status, priority, start_date, due_date, end_date)
                # print(query_str)
                result = self.__cursor.execute(query_str).fetchone()
            self.__unlock()
            return result #.fetchone()

    def insert_annotation(self, annotation, pid, tid=None, anno_type = 0, time_stamp = None):
        # (AID TEXT, TID TEXT, PID TEXT, Annotation CHAR(255), Type INT DEFAULT 1, TimeStamp DATETIME)

        # query_str = "SELECT name FROM ANNOTATION WHERE Name == '%s'" % name
        # print(query_str)
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            # result = self.__cursor.execute(query_str).fetchone()
            # print(result)
            if self.__is_proj_exist(pid) is False and self.__is_task_exist(tid) is False:
                # word is already in the wordbank
                self.__unlock()
                return False
            else:
                aid = self.__get_nex_anno_id()
                if time_stamp is None:
                    today = date.today()
                    time_stamp = today.strftime("%Y-%m-%d %H:%M:%S")
                query_str = "INSERT INTO ANNOTATION (AID, Annotation, PID, TID, Type, TimeStamp) VALUES ('%s', '%s', '%s', '%s', %i, '%s')" % (aid, annotation, pid, tid, anno_type, time_stamp)
                # print(query_str)
                result = self.__cursor.execute(query_str).fetchone()
            self.__unlock()
            return result #.fetchone()

    def empty_line(self):
        ################################################################
        pass
    def get_word(self, word):
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            query_str = "SELECT times, familiar FROM WORD WHERE word == '%s'" % word
            result = self.__cursor.execute(query_str)
            self.__unlock()
            ret_data = result.fetchall()
            if len(ret_data) != 0:
                return ret_data[0]
            else:
                return False
    def update(self, word, times = 1, familiar = 0):
        query_str = "SELECT times, familiar FROM WORD WHERE word == '%s'" % word
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            result = self.__cursor.execute(query_str).fetchone()
            if result is None:
                self.__unlock()
                return False
            else:
                query_str = "UPDATE WORD SET times = %i, familiar = %i WHERE word == '%s'" % (result[0] + times, result[1] + familiar, word)
                result = self.__cursor.execute(query_str).fetchone()
            self.__unlock()
            return result #.fetchone()
    def insert(self, word, familiar = 0):
        query_str = "SELECT word FROM WORD WHERE word == '%s'" % word
        # print(query_str)
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            result = self.__cursor.execute(query_str).fetchone()
            # print(result)
            if result is not None:
                # word is already in the wordbank
                self.__unlock()
                return False
            else:
                query_str = "INSERT INTO WORD (word, times, familiar) VALUES ('%s', %i, %i)" % (word, 1, familiar)
                # print(query_str)
                result = self.__cursor.execute(query_str).fetchone()
            self.__unlock()
            return result #.fetchone()
    def update_familiar(self, word, familiar = 0):
        query_str = "SELECT times, familiar FROM WORD WHERE word == '%s'" % word
        if self.__is_locked():
            # print('db is locked')
            return False
        else:
            self.__lock()
            result = self.__cursor.execute(query_str).fetchone()
            if result is None:
                self.__unlock()
                return False
            else:
                query_str = "UPDATE WORD SET familiar = %i WHERE word == '%s'" % (familiar, word)
                result = self.__cursor.execute(query_str).fetchone()
            self.__unlock()
            return True

if __name__ == '__main__':
    print("Start TaskDB test")
    taskC = TaskDB()
    taskC.connect()

    print("################################################################")
    print("#### Projects Test")
    print("################################################################")
    taskC.insert_project("proj 1", "dsc123")
    taskC.insert_project("proj 2", "dsc123")
    projects = taskC.query_for_all_project()
    print(projects)

    print("################################################################")
    print("#### Task Test")
    print("################################################################")
    taskC.insert_task('P00000000',"task 1 ", "task dsc")
    taskC.insert_task('P00000001',"task 1 ", "task dsc")
    taskC.insert_task('P00000002',"task 1 ", "task dsc")
    task = taskC.query_for_all_task()
    print(task)

    print("################################################################")
    print("#### Anno Test")
    print("################################################################")
    taskC.insert_annotation("project annotation ", pid='P00000000',anno_type=0)
    taskC.insert_annotation("task annotation ", pid='P00000000', tid='T00000000',anno_type=1)
    task = taskC.query_for_all_annotation()
    print(task)

    # taskC.commit()
    taskC.close()
