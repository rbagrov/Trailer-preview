import sqlite3
import syslog

class DB():


    def __init__(self):
        '''
        Init database file and the table
        '''
        self.db = "site_data.db"
        self.table = "trailers"

    def open(self):
        '''
        Opens conncetion to the DB
        '''
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        syslog.syslog('Connection Opened to: ' + str(self.db))
        return [conn,c]

    def get_data(self):
        '''
        Pulls all data from the predefined table and returns it in a tuple for easy iteration
        '''
        _from_open = self.open()
        conn = _from_open[0]
        c = _from_open[1]
        c.execute("SELECT * FROM " + str(self.table) + ";")
        result = c.fetchall()
        syslog.syslog('Pulled all the data from table: ' + str(self.table))
        conn.close()
        syslog.syslog('Connection Closed to: ' + str(self.db))
        return result

    def add(self,data):
        '''
        Takes list containing data for only one movie and uses list index positions as argumets to the sql insert.
        '''
        _from_open = self.open()
        conn = _from_open[0]
        c = _from_open[1]
        c.execute('INSERT INTO trailers VALUES (?,?,?,?,?)', (str(data[0]),str(data[1]),str(data[2]),str(data[3]),str(data[4])))
        conn.commit()
        conn.close()

    def mrproper(self,ensurance):
        '''
        Purely administrative function to safely clean the db.
        Takes a single string argument, so you don't wipe out by accident everything.
        Usage:
        >>>from db import DB
        >>>foo = DB()
        >>>foo.mrproper("Yes I am sure!")
        >>>
        '''
        if ensurance == "Yes I am sure!":
            _from_open = self.open()
            conn = _from_open[0]
            c = _from_open[1]
            c.execute("DELETE FROM " + str(self.table) + ";")
            conn.commit()
            syslog.syslog('Wipe out ' + str(self.db))
            conn.close()
        else:
            pass
