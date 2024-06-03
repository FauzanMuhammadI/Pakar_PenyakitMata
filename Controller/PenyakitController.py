
from mysql.connector import Error
import Model.User
from  Connector.Connector import  ConnectorDatabase

class PenyakitController:
    def Add_Penyakit(self,penyakit):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        hasil = -1

        try:
            Cursor = Con.cursor()
            Query = ("INSERT INTO tabelpenyakit"
                     "(KodePenyakit, NamaPenyakit) "
                     "VALUES (%s, %s)")
            Data_Insert = (penyakit.Getkodepenyakit(),penyakit.Getnamapenyakit())
            Cursor.execute(Query, Data_Insert)
            hasil = Cursor.lastrowid
        except Error as err:
            print(err)
        finally:
            Cursor.close()
            Con.commit()
            Con.close()

        return hasil

    def Getallpenyakit(self):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        Cursor = Con.cursor()
        data = []
        try:

            Query = "SELECT * FROM tabelpenyakit"
            Cursor.execute(Query)
            myresult = Cursor.fetchall()
            for kode, nama in myresult:
                gejala = {"KodeKerusakan": kode, "NamaKerusakan": nama}
                data.append(gejala)


        except Error as err:
            print(err.msg)

        Cursor.close()
        Con.commit()
        Con.close()
        return data

    def edit_Penyekit(self, penyakit):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            hasil = -1

            try:
                Cursor = Con.cursor()
                Query = ("UPDATE tabelpenyakit "
                         "SET NamaPenyakit = %s , KodePenyakit = %s "
                         "WHERE KodePenyakit = %s")
                Data_Update = (penyakit.Getnamapenyakit(), penyakit.Getkodepenyakit(), penyakit.Getkodepenyakit())
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

    def delete_Penyekit(self, kode_penyakit):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            try:
                Cursor = Con.cursor()
                Query = "DELETE FROM tabelpenyakit WHERE KodePenyakit = %s"
                Cursor.execute(Query, (kode_penyakit,))
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



