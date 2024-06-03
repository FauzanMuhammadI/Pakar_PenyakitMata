import mysql.connector

class ConnectorDatabase:
    def __init__(self):

        self.db = None
    def Conennect(self):
        try:
           self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pakar_db"
            )
        except mysql.connector.Error as err:
            print(err.msg)

        if(self.db == None):
            print("DataBase Not Connect")
        else:
            print("DataBase Connect ")
        return self.db

    def CloseConnect(self):
        try:
           self.db.close()
        except mysql.connector.Error as err:
            print(err.msg)
