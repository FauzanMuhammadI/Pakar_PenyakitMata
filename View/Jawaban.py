import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog
from PyQt5.uic import loadUi
from pyqt5_plugins.examplebuttonplugin import QtGui

from Controller.JawabanController import JawabanController
from Controller.PertanyaanController import PertanyaanController
from Model.Jawaban import JawabanModel


class Jawaban(QtWidgets.QMainWindow):
    def __init__(self):
        super(Jawaban, self).__init__()
        loadUi('Jawaban_view.ui', self)
        self.pertanyaan = JawabanController()

        try:
            self.Show_Pertanyaan()
        except Exception as e:
            print(e)
        self.Tambah_btn_8.clicked.connect(self.gambar)
        self.Tambah_btn_5.clicked.connect(self.jawaban)
        self.deletepenyakit_btn_2.clicked.connect(self.delete)
        self.tableWidget.itemClicked.connect(self.on_item_clicked1)
        self.kodejawaban = None
        self.img = None
    def delete(self):
        hasil = self.pertanyaan.Delete_Jawaban( self.kodejawaban)
        self.Show_Pertanyaan()

    def on_item_clicked1(self, item):
        row = item.row()
        col = item.column()

        kode = self.tableWidget.item(row, 0).text()  # Mendapatkan kode penyakit dari item yang dipilih
        jawaban = self.tableWidget.item(row, 1).text()  # Mendapatkan nama penyakit dari item yang dipilih
        self.kodejawaban = kode
        self.Kode_edt_2.setText(kode)
        self.Kode_edt_3.setText(jawaban)
        self.Kode_edt_4.setText(self.tableWidget.item(row, 3).text())

        pixmap = self.tableWidget.cellWidget(row,2).pixmap()
        self.label_7.setPixmap(pixmap)
        self.label_7.adjustSize()
    def jawaban(self):
        kode = self.Kode_edt_2.text()
        jawaban = self.Kode_edt_3.text()
        kerusakan = self.Kode_edt_4.text()
        jwb = JawabanModel(kode,self.img,jawaban,kerusakan)
        print(self.img)
        hasil = self.pertanyaan.Add_Jawaban(jwb)
        self.Show_Pertanyaan()
        self.Tambah_btn_5.setEnabled(False)

    def gambar(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        img, _ = QFileDialog.getOpenFileName(self, "Select Image", "",
                                                    "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if img:
            self.img = self.get_blob_from_file(img)
            pixmap = QtGui.QPixmap(img)
            self.label_7.setPixmap(pixmap)
            self.label_7.adjustSize()
            self.Tambah_btn_5.setEnabled(True)

    def get_blob_from_file(self, file_path):
        with open(file_path, "rb") as file:
            blob_data = file.read()
        return blob_data

    def get_pixmap_from_blob(self, blob_data):
        image = QtGui.QImage.fromData(blob_data)
        pixmap = QtGui.QPixmap.fromImage(image)
        return pixmap

    def Show_Pertanyaan(self):
        data = self.pertanyaan.GetAllJawaban()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(["Kode Pertanyaan", "Jawaban", "Gambar", "Kode Kerusakan"])
        self.tableWidget.setStyleSheet("QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section { background-color: #393E46; color : #fff }")
        self.tableWidget.setRowCount(len(data))
        for row, pertanyaan in enumerate(data):
            kode_pertanyaan = pertanyaan["KodeJawaban"]
            jawaban = pertanyaan["Teks"]
            gambar = pertanyaan["Gambar"]  # Assuming gambar contains image data as bytes
            kode_kerusakan = pertanyaan["KodeKerusakan"]
            kode_item = QTableWidgetItem(kode_pertanyaan)
            jawaban_item = QTableWidgetItem(jawaban)
            kode_item.setForeground(QtGui.QColor("#fff"))
            jawaban_item.setForeground(QtGui.QColor("#fff"))
            self.tableWidget.setItem(row, 0, kode_item)
            self.tableWidget.setItem(row, 1, jawaban_item)

            # Displaying image from bytes
            pixmap = self.get_pixmap_from_blob(gambar)
            label = QtWidgets.QLabel()
            label.setPixmap(pixmap)
            self.tableWidget.setCellWidget(row, 2, label)

            kode_kerusakan_item = QTableWidgetItem(kode_kerusakan)
            kode_kerusakan_item.setForeground(QtGui.QColor("#fff"))
            self.tableWidget.setItem(row, 3, kode_kerusakan_item)
