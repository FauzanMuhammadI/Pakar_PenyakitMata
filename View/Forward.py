import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from pyqt5_plugins.examplebuttonplugin import QtGui
from gtts import gTTS
import os
import pygame
from io import BytesIO
from Controller.JawabanController import JawabanController
from Controller.PenyakitController import PenyakitController
from Controller.PertanyaanController import PertanyaanController
from Controller.RuleController import RuleController
from Controller.UserController import UserController
from Model.User import UserModel
from View.Admin import Admin

class Forward(QtWidgets.QMainWindow):
    def __init__(self):
        super(Forward, self).__init__()
        loadUi('Forward.ui', self)
        self.pertanyaan = PertanyaanController()
        self.rule = RuleController()
        self.jawaban = JawabanController()
        self.Diagnosa_btn.clicked.connect(self.Mulai_diagnosa)
        self.Ya_btn.clicked.connect(self.ya)
        self.Tidak_btn.clicked.connect(self.tidak)
        self.label_7.setWordWrap(True)
        self.workinglist = []
        # self.workinglist.add
        self.i = 0
        self.i1 = 0
    def Mulai_diagnosa(self):
        data= self.pertanyaan.GetallPertanyaan()
        self.Ya_btn.setEnabled(True)
        self.Tidak_btn.setEnabled(True)
        self.Kode_edt_3.clear()

        if len(self.listWidget) == data  :
            self.Showpertanyaan(self.i)
        else:
            self.workinglist = []
            self.i = 0
            self.i1 = 0
            self.listWidget.clear()
            self.Showpertanyaan(self.i)

    def Showpertanyaan(self,i):
        data= self.pertanyaan.GetallPertanyaan()
        if self.i < len(data) :
            self.i1 = i
            self.listWidget.addItem(data[i]["Nama"])
            # self.Kode_edt_3.setText("Maaf, tidak ada penyakit yang terdeteksi")
    def ya(self):
        data = self.pertanyaan.GetallPertanyaan()
        self.workinglist.append(data[self.i1]["Kode"])

        self.i += 1
        self.Showpertanyaan(self.i)
        if self.i == len(data) :
            self.prosses(self.workinglist)


        # else:
        print(self.i)

    def tidak(self):
        data = self.pertanyaan.GetallPertanyaan()

        if self.i == len(data) :
            self.prosses(self.workinglist)
        self.i += 1
        self.Showpertanyaan(self.i)

        # else:
            # self.prosses(set(self.workinglist))

        print(self.workinglist)

    def prosses(self, workinglist):
        data = self.rule.Getallrule()
        penyakit_ditemukan = False
        kode_penyakit = None

        if workinglist:
            for pertanyaan in data:

                kode = "".join(workinglist)
                print(kode)
                if kode == pertanyaan['KodePertanyaan'].replace(",","") :
                    kode_penyakit = pertanyaan['KodeKerusakan']
                    penyakit_ditemukan = True
                    break


        if not penyakit_ditemukan:
            self.Kode_edt_3.setText("Maaf, tidak ada penyakit yang terdeteksi")
        else:
            penyakit = PenyakitController()
            self.Penjelasan(kode_penyakit)

            data_penyakit = penyakit.Getallpenyakit()
            for item in data_penyakit:
                if item['KodeKerusakan'] in kode_penyakit:
                    self.Kode_edt_3.setText(item['NamaKerusakan'])
        self.Ya_btn.setEnabled(False)
        self.Tidak_btn.setEnabled(False)

    def get_pixmap_from_blob(self, blob_data):
        image = QtGui.QImage.fromData(blob_data)
        pixmap = QtGui.QPixmap.fromImage(image)
        return pixmap

    def Penjelasan(self,kode_penyakit):
        data = self.jawaban.GetJawaban_forward(kode_penyakit)
        print("test")
        kata = None
        for item  in data:
            gambar = item["Gambar"]
            teks = item["Teks"]
            kata = teks
            self.label_7.setText(teks)
            pixmap = self.get_pixmap_from_blob(gambar)
            # label = QtWidgets.QLabel()
            self.label_8.setPixmap(pixmap)
            # self.setCentralWidget(self.label_8)
            # self.resize(pixmap.width(), pixmap.height())
        self.TTS(kata)

    def TTS(self,teks):

        tts = gTTS(text=teks, lang='id')

        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        pygame.mixer.init()
        pygame.mixer.music.load(audio_bytes)
        pygame.mixer.music.play()

        # Tunggu hingga audio selesai diputar
        # while pygame.mixer.music.get_busy():
        #     continue

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Forward()
    mainWindow.show()
    sys.exit(app.exec_())

