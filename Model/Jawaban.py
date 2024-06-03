class JawabanModel:
    def __init__(self, KodeJawaban, gambar, teks, KodeKerusakan):
        self._KodeJawaban = KodeJawaban
        self._gambar = gambar
        self._teks = teks
        self._KodeKerusakan = KodeKerusakan

    def GetKodeJawaban(self):
        return self._KodeJawaban

    def GetGambar(self):
        return self._gambar

    def GetTeks(self):
        return self._teks

    def GetKodeKerusakan(self):
        return self._KodeKerusakan
