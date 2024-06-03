import sys
import cv2
import numpy as np
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from pyqt5_plugins.examplebuttonplugin import QtGui

from Controller.GejalaController import GejalaController
from Controller.PenyakitController import PenyakitController
from Controller.PertanyaanController import PertanyaanController
from Controller.RuleController import RuleController
from Model.Gejala import GejalaModel
from Model.Penyakit import PenyakitModel
from Model.Pertamyaan import PertanyaanModel
from Model.Rule import RuleModel
from View.Jawaban import Jawaban


# from View.Jawaban import Jawaban


class Admin(QMainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        loadUi('Admin_view.ui', self)
        self.penyakit = PenyakitController()
        self.gejala = GejalaController()
        self.pertanyaan = PertanyaanController()
        self.rule = RuleController()


        self.Show_Penyakit()
        self.Show_gejala()
        self.Show_pertanyaan()
        self.Show_rule()

        #Penyakit
        self.Tambah_btn.clicked.connect(self.Add_penyakit)
        self.Editpenyakit_btn.clicked.connect(self.edt_penyakit)
        self.deletepenyakit_btn.clicked.connect(self.delete_penyakit)
        self.tableWidget.itemClicked.connect(self.on_item_clicked)
        self.kodepenyakit = None


        #Gejala
        self.Tambah_btn_2.clicked.connect(self.Add_gejala)
        self.edt_btn.clicked.connect(self.Edit_gejala)
        self.deletegejala_btn.clicked.connect(self.delete_gejala)
        self.tableWidget_2.itemClicked.connect(self.on_item_clicked1)
        self.kodegejala = None

        # Pertanyaan
        self.Tambah_btn_3.clicked.connect(self.Add_pertanyaan)
        self.edt_btn_2.clicked.connect(self.Edit_pertanyaan)
        self.delete_btn_2.clicked.connect(self.delete_pertanyaan)
        self.tableWidget_3.itemClicked.connect(self.on_item_clicked2)
        self.kodepertanyaan = None

        # Rule
        self.Tambah_btn_4.clicked.connect(self.Add_Rule)
        self.edt_btn_3.clicked.connect(self.Edit_rule)
        self.delete_btn_3.clicked.connect(self.delete_rule)
        self.tableWidget_4.itemClicked.connect(self.on_item_clicked3)
        self.koderule = None

        self.Lanjut_btn.clicked.connect(self.lanjut)
        self.Kembal_btn.clicked.connect(self.kembali)



    def lanjut(self):
        try :
            self.jawaban = Jawaban()
            self.jawaban.show()
            self.hide()
        except Exception as e:
            print(e)
    def kembali(self):
        from View.Login import showimage

        self.login = showimage()
        self.login.show()
        self.hide()

    def lanjut(self):
        self.jawaban = Jawaban()
        self.jawaban.show()
        self.hide()
    def Add_Rule(self):
        nm = self.edt_5.text()
        kode_nm = self.edt_4.text()
        prt = self.edt_6.text()
        pyk = RuleModel(kode_nm, nm,prt)
        hasil = self.rule.Add_Rule(pyk)
        self.Show_rule()
        self.edt_5.clear()
        self.edt_4.clear()
        self.edt_6.clear()
    def Edit_rule(self):
        nm = self.edt_5.text()
        kode_nm = self.edt_4.text()
        prt = self.edt_6.text()
        pyk = RuleModel(kode_nm, nm, prt)
        hasil = self.rule.edit_rule(pyk)
        self.Show_rule()
        self.edt_5.clear()
        self.edt_4.clear()
        self.edt_6.clear()

    def Show_rule(self):
        data = self.rule.Getallrule()
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setHorizontalHeaderLabels(["Kode Rule", "Kode Pertanyaan", "Kode Penyakit"])
        self.tableWidget_4.setStyleSheet("QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget_4.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget_4.setRowCount(len(data))
        for row, gejala in enumerate(data):
            kode_gejala = gejala["Kode"]
            kode_pertanyaan = gejala["KodePertanyaan"]
            kode_penyakit = gejala["KodeKerusakan"]
            kode_item = QTableWidgetItem(kode_gejala)
            nama_item = QTableWidgetItem(kode_pertanyaan)
            penyakit = QTableWidgetItem(kode_penyakit)
            kode_item.setForeground(QtGui.QColor("#fff"))
            nama_item.setForeground(QtGui.QColor("#fff"))
            penyakit.setForeground(QtGui.QColor("#fff"))
            self.tableWidget_4.setItem(row, 0, kode_item)  # Mengubah dari tableWidget_3 ke tableWidget_4
            self.tableWidget_4.setItem(row, 1, nama_item)  # Mengubah dari tableWidget_3 ke tableWidget_4
            self.tableWidget_4.setItem(row, 2, penyakit)  # Mengubah dari tableWidget_3 ke tableWidget_4

    def delete_pertanyaan(self):
        hasil = self.rule.delete_Rule(self.edt_4.text())
        if hasil != -1:
            self.label_4.setText("Berhasil di hapus")
        self.Show_rule()
    def on_item_clicked3(self, item):
        row = item.row()
        col = item.column()

        kode = self.tableWidget_4.item(row, 0).text()  # Mendapatkan kode rule dari item yang dipilih
        kode_pertanyaan = self.tableWidget_4.item(row, 1).text()  # Mendapatkan kode pertanyaan dari item yang dipilih
        kode_penyakit = self.tableWidget_4.item(row, 2).text()  # Mendapatkan kode penyakit dari item yang dipilih

        self.koderule = kode  # Mengatur kode rule ke variabel koderule
        self.edt_4.setText(kode)  # Menetapkan kode rule ke edt_4
        self.edt_5.setText(kode_pertanyaan)  # Menetapkan kode pertanyaan ke edt_5
        self.edt_6.setText(kode_penyakit)  # Menetapkan kode penyakit ke edt_6

    def Add_pertanyaan(self):
        nm = self.edt_2.text()
        kode_nm = self.edt_3.text()
        pyk = PertanyaanModel(kode_nm, nm)
        hasil = self.pertanyaan.Add_Pertanyaan(pyk)
        self.Show_pertanyaan()
        self.edt_2.clear()
        self.edt_3.clear()
    def Edit_pertanyaan(self):
        nm= self.edt_2.text()
        kode_nm = self.edt_3.text()
        pyk = PertanyaanModel(kode_nm,nm)
        hasil = self.pertanyaan.edit_Pertanyaan(pyk)
        self.Show_pertanyaan()
        self.edt_2.clear()
        self.edt_3.clear()
    def Show_pertanyaan(self):
        data = self.pertanyaan.GetallPertanyaan()
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setHorizontalHeaderLabels(["Kode Pertanyaan", "Nama Pertanyaan"])
        self.tableWidget_3.setStyleSheet("QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget_3.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget_3.setRowCount(len(data))
        for row, gejala in enumerate(data):
            kode_gejala = gejala["Kode"]
            nama_gejala = gejala["Nama"]
            kode_item = QTableWidgetItem(kode_gejala)
            nama_item = QTableWidgetItem(nama_gejala)
            kode_item.setForeground(QtGui.QColor("#fff"))
            nama_item.setForeground(QtGui.QColor("#fff"))
            self.tableWidget_3.setItem(row, 0, kode_item)
            self.tableWidget_3.setItem(row, 1, nama_item)
    def delete_rule(self):
        hasil = self.pertanyaan.delete_Pertanyaan(self.edt_3.text())
        if hasil != -1:
            self.label_4.setText("Berhasil di hapus")
        self.Show_pertanyaan()
    def on_item_clicked2(self, item):

        row = item.row()
        col = item.column()

        kode = self.tableWidget_3.item(row, 0).text()  # Mendapatkan kode penyakit dari item yang dipilih
        nama = self.tableWidget_3.item(row, 1).text()  # Mendapatkan nama penyakit dari item yang dipilih
        self.kodepertanyaan = kode
        self.edt_2.setText(nama)
        self.edt_3.setText(kode)

    ###################################################################Pertanyaan#################
    def Add_gejala(self):
        nm = self.namagejala_edt.text()
        kode_nm = self.gejala_edt.text()
        pyk = GejalaModel(kode_nm, nm)
        hasil = self.gejala.Add_Gejala(pyk)
        self.Show_gejala()
        self.gejala_edt.clear()
        self.namagejala_edt.clear()
    def Edit_gejala(self):
        nm= self.namagejala_edt.text()
        kode_nm = self.gejala_edt.text()
        pyk = GejalaModel(kode_nm,nm)
        hasil = self.gejala.edit_Gejala(pyk)
        print(hasil)
        self.Show_gejala()
        self.namagejala_edt.clear()
        self.gejala_edt.clear()
    def Show_gejala(self):
        data = self.gejala.Getallgejala()
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setHorizontalHeaderLabels(["Kode Gejala", "Nama Gejala"])
        self.tableWidget_2.setStyleSheet("QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget_2.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget_2.setRowCount(len(data))
        for row, gejala in enumerate(data):
            kode_gejala = gejala["Kode"]
            nama_gejala = gejala["Nama"]
            kode_item = QTableWidgetItem(kode_gejala)
            nama_item = QTableWidgetItem(nama_gejala)
            kode_item.setForeground(QtGui.QColor("#fff"))
            nama_item.setForeground(QtGui.QColor("#fff"))
            self.tableWidget_2.setItem(row, 0, kode_item)
            self.tableWidget_2.setItem(row, 1, nama_item)
    def delete_gejala(self):
        hasil = self.gejala.delete_Gejala(self.gejala_edt.text())
        if hasil != -1:
            self.label_4.setText("Berhasil di hapus")
        self.Show_gejala()
    def on_item_clicked1(self, item):
        row = item.row()
        col = item.column()

        kode = self.tableWidget_2.item(row, 0).text()  # Mendapatkan kode penyakit dari item yang dipilih
        nama = self.tableWidget_2.item(row, 1).text()  # Mendapatkan nama penyakit dari item yang dipilih
        self.kodegejala = kode
        self.namagejala_edt.setText(nama)
        self.gejala_edt.setText(kode)

    def delete_penyakit(self):
        hasil = self.penyakit.delete_Penyekit(self.Kode_edt.text())
        if hasil != -1:
            self.label_4.setText("Berhasil di hapus")
        self.Show_Penyakit()
    def on_item_clicked(self, item):
        row = item.row()
        col = item.column()

        kode_penyakit = self.tableWidget.item(row, 0).text()  # Mendapatkan kode penyakit dari item yang dipilih
        nama_penyakit = self.tableWidget.item(row, 1).text()  # Mendapatkan nama penyakit dari item yang dipilih
        self.kodepenyakit = kode_penyakit
        self.Penyakit_edt.setText(nama_penyakit)
        self.Kode_edt.setText(kode_penyakit)

    def Add_penyakit(self):
        penyakit_nm = self.Penyakit_edt.text()
        kode_nm = self.Kode_edt.text()
        pyk = PenyakitModel(kode_nm, penyakit_nm)
        hasil = self.penyakit.Add_Penyakit(pyk)
        self.Show_Penyakit()
        self.Penyakit_edt.clear()
        self.Kode_edt.clear()  # Menghapus teks dari QLineEdit 'Kode_edt'

    def Edit_penyakit(self):
        penyakit_nm= self.Penyakit_edt.text()
        kode_nm = self.Kode_edt.text()
        pyk = PenyakitModel(kode_nm,penyakit_nm)
        hasil = self.penyakit.edit_Penyekit(pyk)
        self.Show_Penyakit()
        self.Penyakit_edt.clear()
        self.Kode_edt.text().clear()
    def Show_Penyakit(self):
        data = self.penyakit.Getallpenyakit()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Kode Penyakit", "Nama Penyakit"])
        self.tableWidget.setStyleSheet("QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget.setRowCount(len(data))
        for row, gejala in enumerate(data):
            kode_gejala = gejala["KodeKerusakan"]
            nama_gejala = gejala["NamaKerusakan"]
            kode_item = QTableWidgetItem(kode_gejala)
            nama_item = QTableWidgetItem(nama_gejala)
            kode_item.setForeground(QtGui.QColor("#fff"))
            nama_item.setForeground(QtGui.QColor("#fff"))
            self.tableWidget.setItem(row, 0, kode_item)
            self.tableWidget.setItem(row, 1, nama_item)
    def edt_penyakit(self):
        kode = self.Kode_edt.text()
        nama = self.Penyakit_edt.text()
        pnykt = PenyakitModel(kode,nama)
        hasil = self.penyakit.edit_Penyekit(pnykt)
        if hasil != -1 :
            self.label_4.setText("Berhasil Di Edit")
        else:
            self.label_4.setText("Gagal Di Edit")
        self.Show_Penyakit()