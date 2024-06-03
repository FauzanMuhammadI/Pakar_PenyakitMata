class PenyakitModel:
    def __init__(self,kodepenyakit,namapenyakit):
        self.__kodepenyakit = kodepenyakit
        self.__namapenyakit = namapenyakit
    def Getnamapenyakit(self):
        return self.__namapenyakit
    def Getkodepenyakit(self):
        return self.__kodepenyakit
    def Setnamapenyakit(self,namapenyakit):
        self.__namapenyakit = namapenyakit
    def Setkodepenyakit(self,kodegejala):
        self.__kodepenyakit = kodegejala