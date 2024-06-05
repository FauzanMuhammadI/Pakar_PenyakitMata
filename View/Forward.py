import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi
from gtts import gTTS
import pygame
from io import BytesIO
from Controller.JawabanController import JawabanController
from Controller.PenyakitController import PenyakitController
from Controller.PertanyaanController import PertanyaanController
from Controller.RuleController import RuleController

class Forward(QtWidgets.QMainWindow):
    def __init__(self):
        super(Forward, self).__init__()
        loadUi('Forward.ui', self)
        self.pertanyaan = PertanyaanController()
        self.rule = RuleController()
        self.jawaban = JawabanController()
        self.tabelRuleWindow = None  # Initialize with None
        self.Diagnosa_btn.clicked.connect(self.Mulai_diagnosa)
        self.Rule_btn.clicked.connect(self.tabel_rule)
        self.Ya_btn.clicked.connect(self.ya)
        self.Tidak_btn.clicked.connect(self.tidak)
        self.label_7.setWordWrap(True)
        self.workinglist = []
        self.i = 0
        self.i1 = 0

    def Mulai_diagnosa(self):
        data = self.pertanyaan.GetallPertanyaan()
        self.Ya_btn.setEnabled(True)
        self.Tidak_btn.setEnabled(True)
        self.Kode_edt_3.clear()

        if len(self.listWidget) == data:
            self.Showpertanyaan(self.i)
        else:
            self.workinglist = []
            self.i = 0
            self.i1 = 0
            self.listWidget.clear()
            self.Showpertanyaan(self.i)

    def Showpertanyaan(self, i):
        data = self.pertanyaan.GetallPertanyaan()
        if self.i < len(data):
            self.i1 = i
            self.listWidget.addItem(data[i]["Nama"])

    def ya(self):
        data = self.pertanyaan.GetallPertanyaan()
        self.workinglist.append(data[self.i1]["Kode"])

        self.i += 1
        self.Showpertanyaan(self.i)
        if self.i == len(data):
            self.prosses(self.workinglist)

        print(self.i)

    def tidak(self):
        data = self.pertanyaan.GetallPertanyaan()

        if self.i == len(data):
            self.prosses(self.workinglist)
        self.i += 1
        self.Showpertanyaan(self.i)

        print(self.workinglist)

    def prosses(self, workinglist):
        data = self.rule.Getallrule()
        penyakit_ditemukan = False
        kode_penyakit = None

        if workinglist:
            for pertanyaan in data:
                kode = "".join(workinglist)
                print(kode)
                if kode == pertanyaan['KodePertanyaan'].replace(",", ""):
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

    def Penjelasan(self, kode_penyakit):
        data = self.jawaban.GetJawaban_forward(kode_penyakit)
        print("test")
        kata = None
        for item in data:
            gambar = item["Gambar"]
            teks = item["Teks"]
            kata = teks
            self.label_7.setText(teks)
            pixmap = self.get_pixmap_from_blob(gambar)
            self.label_8.setPixmap(pixmap)
        self.TTS(kata)

    def TTS(self, teks):
        tts = gTTS(text=teks, lang='id')
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        pygame.mixer.init()
        pygame.mixer.music.load(audio_bytes)
        pygame.mixer.music.play()

    def tabel_rule(self):
        if self.tabelRuleWindow is None:
            self.tabelRuleWindow = TabelRuleWindow()
        self.tabelRuleWindow.show()


class TabelRuleWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(TabelRuleWindow, self).__init__()
        loadUi('TabelRule.ui', self)

    def showEvent(self, event):
        super().showEvent(event)
        self.tableWidget.resizeColumnsToContents()

        extra_space_default = 10
        extra_space_kode_pertanyaan = 20
        for col in range(self.tableWidget.columnCount()):
            current_width = self.tableWidget.columnWidth(col)
            if col == 1:
                self.tableWidget.setColumnWidth(col, current_width + extra_space_kode_pertanyaan)
            else:
                self.tableWidget.setColumnWidth(col, current_width + extra_space_default)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Forward()
    mainWindow.show()
    sys.exit(app.exec_())
