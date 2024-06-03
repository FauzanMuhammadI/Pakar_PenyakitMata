
from mysql.connector import Error
import Model.User
from  Connector.Connector import  ConnectorDatabase

class PertanyaanController:
    def Add_Pertanyaan(self,Pertanyaan):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        hasil = -1

        try:
            Cursor = Con.cursor()


            Query = ("INSERT INTO tabelpertanyaan "
                     "(KodePertanyaan, Pertanyaan) "
                     "VALUES (%s, %s)")
            Data_Insert = ( Pertanyaan.GetkodePertanyaan(),Pertanyaan.GetnamaPertanyaan())
            Cursor.execute(Query, Data_Insert)
            hasil = Cursor.lastrowid
        except Error as err:
            print(err)
        finally:
            Cursor.close()
            Con.commit()
            Con.close()

        return hasil
    def GetallPertanyaan(self):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        Cursor = Con.cursor()
        data = []
        try:

            Query = "SELECT * FROM tabelpertanyaan"
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

    def edit_Pertanyaan(self, Pertanyaan):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            hasil = -1

            try:
                Cursor = Con.cursor()
                Query = ("UPDATE tabelpertanyaan "
                         "SET Pertanyaan = %s , KodePertanyaan = %s "
                         "WHERE KodePertanyaan = %s")
                Data_Update = (Pertanyaan.GetnamaPertanyaan(), Pertanyaan.GetkodePertanyaan(), Pertanyaan.GetkodePertanyaan())
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

    def delete_Pertanyaan(self, kode_Pertanyaan):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            try:
                Cursor = Con.cursor()
                Query = "DELETE FROM tabelpertanyaan WHERE KodePertanyaan = %s"
                Cursor.execute(Query, (kode_Pertanyaan,))
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


