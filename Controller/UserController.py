from mysql.connector import Error
import Model.User
from  Connector.Connector import  ConnectorDatabase


class UserController:
    def Logic_Register(self, user):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        hasil = -1

        try:
            Cursor = Con.cursor()

            # Memeriksa apakah nama pengguna sudah ada
            Query_Check = ("SELECT COUNT(*) FROM user WHERE Name = %s")
            Data_Check = (user.Getname(),)
            Cursor.execute(Query_Check, Data_Check)
            result = Cursor.fetchone()

            # Jika nama pengguna sudah ada, kembalikan nilai -1
            if result[0] > 0:
                hasil = -1
            else:
                Query_Insert = ("INSERT INTO user "
                                "(Name, Password) "
                                "VALUES (%s, %s)")
                Data_Insert = (user.Getname(), user.Getpassword())
                Cursor.execute(Query_Insert, Data_Insert)
                hasil = Cursor.lastrowid
                hasil = 1
        except Error as err:
            print(err)
        finally:
            Cursor.close()
            Con.commit()
            Con.close()

        return hasil

    def Logic_Login(self,user):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        hasil = 1
        Cursor = Con.cursor()
        print("Asd")

        try:
            Query = "SELECT * FROM user WHERE Name = %s  AND Password = %s"
            Data_Insert = (user.Getname(), user.Getpassword())
            Cursor.execute(Query, Data_Insert)
            myresult  = Cursor.fetchall()
            # print()
            if user.Getname() == "Admin"  and user.Getpassword() == "Admin":
                hasil = 0
                print("Berhasil")
            elif len(myresult) <= 0 :
                hasil = -1
            else:
                hasil = myresult[0][0]
        except Error as err:
            print(err.msg)

        Cursor.close()
        Con.commit()
        Con.close()
        return hasil