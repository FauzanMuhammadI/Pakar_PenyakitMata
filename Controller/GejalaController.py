
from mysql.connector import Error
import Model.User
from  Connector.Connector import  ConnectorDatabase

class GejalaController:
    def Add_Gejala(self,gejala):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        hasil = -1

        try:
            Cursor = Con.cursor()


            Query = ("INSERT INTO tabelgejala "
                     "(KodeGejala, NamaGejala) "
                     "VALUES (%s, %s)")
            Data_Insert = ( gejala.Getkodegejala(),gejala.Getnamagejala())
            Cursor.execute(Query, Data_Insert)
            hasil = Cursor.lastrowid
        except Error as err:
            print(err)
        finally:
            Cursor.close()
            Con.commit()
            Con.close()

        return hasil
    def Getallgejala(self):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        Cursor = Con.cursor()
        data = []
        try:

            Query = "SELECT * FROM tabelgejala"
            Cursor.execute(Query)
            myresult  = Cursor.fetchall()
            for kode,nama in myresult:
                gejala = {"Kode": kode, "Nama": nama}
                data.append(gejala)


        except Error as err:
            print(err.msg)

        Cursor.close()
        Con.commit()
        Con.close()
        return data

    def edit_Gejala(self, gejala):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            hasil = -1

            try:
                Cursor = Con.cursor()
                Query = ("UPDATE tabelgejala "
                         "SET NamaGejala = %s , KodeGejala = %s "
                         "WHERE KodeGejala = %s")
                Data_Update = (gejala.Getnamagejala(), gejala.Getkodegejala(), gejala.Getkodegejala())
                Cursor.execute(Query, Data_Update)
                hasil = Cursor.rowcount
            except Error as err:
                print(err)
            finally:
                Cursor.close()
                Con.commit()
                Con.close()

            return hasil
        except Exception as e:
            print("Error:", e)
            return -1

    def delete_Gejala(self, kode_gejala):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            try:
                Cursor = Con.cursor()
                Query = "DELETE FROM tabelgejala WHERE KodeGejala = %s"
                Cursor.execute(Query, (kode_gejala,))
                hasil = Cursor.rowcount
            except Error as err:
                print(err)
                hasil = -1
            finally:
                Cursor.close()
                Con.commit()
                Con.close()

            return hasil
        except Exception as e:
            print("Error:", e)
            return -1


