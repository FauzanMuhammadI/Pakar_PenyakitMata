class RuleModel:
    def __init__(self,koderule,kodepertanyaan,kodepenyakit):
        self.__koderule = koderule
        self.__kodepertanyaan = kodepertanyaan
        self.__kodepenyakit = kodepenyakit

    def GetKoderule(self):
        return self.__koderule

    def GetKodepertanyaan(self):
        return self.__kodepertanyaan

    def GetKodepenyakit(self):
        return self.__kodepenyakit

    def SetKoderule(self, koderule):
        self.__koderule = koderule

    def SetKodepertanyaan(self, kodepertanyaan):
        self.__kodepertanyaan = kodepertanyaan

    def SetKodepenyakit(self, kodepenyakit):
        self.__kodepenyakit = kodepenyakit