from Connector.Connector import ConnectorDatabase
from mysql.connector import Error


class JawabanController:
    def Add_Jawaban(self, jawaban):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        hasil = -1

        try:
            Cursor = Con.cursor()

            Query = ("INSERT INTO tablejawaban "
                     "(KodeJawaban, Gambar, Teks, KodeKerusakan) "
                     "VALUES (%s, %s, %s, %s)")
            Data_Insert = (jawaban.GetKodeJawaban(), jawaban.GetGambar(), jawaban.GetTeks(), jawaban.GetKodeKerusakan())
            Cursor.execute(Query, Data_Insert)
            hasil = Cursor.lastrowid
        except Error as err:
            print(err)
        finally:
            Cursor.close()
            Con.commit()
            Con.close()

        return hasil

    def GetAllJawaban(self):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        Cursor = Con.cursor()
        data = []
        try:
            Query = "SELECT * FROM tablejawaban"
            Cursor.execute(Query)
            myresult = Cursor.fetchall()
            for kode, gambar, teks, kode_kerusakan in myresult:
                jawaban_data = {"KodeJawaban": kode, "Gambar": gambar, "Teks": teks, "KodeKerusakan": kode_kerusakan}
                data.append(jawaban_data)
        except Error as err:
            print(err.msg)
        finally:
            Cursor.close()
            Con.commit()
            Con.close()
        return data

    def Edit_Jawaban(self, jawaban):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            hasil = -1

            try:
                Cursor = Con.cursor()
                Query = ("UPDATE tabeljawaban "
                         "SET gambar = %s, Teks = %s, KodeKerusakan = %s "
                         "WHERE KodeJawaban = %s")
                Data_Update = (jawaban.GetGambar(), jawaban.GetTeks(), jawaban.GetKodeKerusakan(), jawaban.GetKodeJawaban())
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

    def Delete_Jawaban(self, kode_jawaban):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            try:
                Cursor = Con.cursor()
                Query = "DELETE FROM tablejawaban WHERE KodeJawaban = %s"
                Cursor.execute(Query, (kode_jawaban,))
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

    def GetJawaban_forward(self,kode):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        Cursor = Con.cursor()
        data = []
        try:
            Query = "SELECT * FROM tablejawaban WHERE KodeKerusakan = %s"
            Cursor.execute(Query,(kode,))
            myresult = Cursor.fetchall()
            for kode, gambar, teks, kode_kerusakan in myresult:
                jawaban_data = {"Gambar": gambar, "Teks": teks}
                data.append(jawaban_data)
        except Error as err:
            print(err.msg)
        finally:
            Cursor.close()
            Con.commit()
            Con.close()
        return data