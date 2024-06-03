
from mysql.connector import Error
import Model.User
from  Connector.Connector import  ConnectorDatabase

class RuleController:
    def Add_Rule(self,Rule):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        hasil = -1

        try:
            Cursor = Con.cursor()


            Query = ("INSERT INTO tabelrule "
                     "(KodeRule, kodepertanyaan1,kodepenyakit) "
                     "VALUES (%s, %s, %s)")
            Data_Insert = ( Rule.GetKoderule(),Rule.GetKodepertanyaan(),Rule.GetKodepenyakit())
            Cursor.execute(Query, Data_Insert)
            hasil = Cursor.lastrowid
        except Error as err:
            print(err)
        finally:
            Cursor.close()
            Con.commit()
            Con.close()

        return hasil
    def Getallrule(self):
        cn = ConnectorDatabase()
        Con = cn.Conennect()

        Cursor = Con.cursor()
        data = []
        try:

            Query = "SELECT * FROM tabelrule"
            Cursor.execute(Query)
            myresult  = Cursor.fetchall()
            for kode,pertanyaan,kerusakan in myresult:
                gejala = {"Kode": kode, "KodePertanyaan": pertanyaan ,"KodeKerusakan": kerusakan }
                data.append(gejala)


        except Error as err:
            print(err.msg)

        Cursor.close()
        Con.commit()
        Con.close()
        return data

    def edit_rule(self, Rule):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            hasil = -1

            try:
                Cursor = Con.cursor()
                Query = ("UPDATE tabelrule "
                         "SET KodeRule = %s ,kodepertanyaan1 = %s , kodepenyakit = %s "
                         "WHERE KodeRule = %s")
                Data_Update = (Rule.GetKoderule(),Rule.GetKodepertanyaan(),Rule.GetKodepenyakit())
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

    def delete_Rule(self, kode_rule):
        try:
            cn = ConnectorDatabase()
            Con = cn.Conennect()

            try:
                Cursor = Con.cursor()
                Query = "DELETE FROM tabelrule WHERE KodeRule = %s"
                Cursor.execute(Query, (kode_rule,))
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


