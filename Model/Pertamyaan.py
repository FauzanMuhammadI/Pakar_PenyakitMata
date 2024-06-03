class PertanyaanModel:
    def __init__(self,kodePertanyaan,namaPertanyaan):
        self.__kodePertanyaan = kodePertanyaan
        self.__namaPertanyaan = namaPertanyaan
        
    def GetnamaPertanyaan(self):
        return self.__namaPertanyaan
    def GetkodePertanyaan(self):
        return self.__kodePertanyaan
    def SetnamaPertanyaan(self,namaPertanyaan):
        self.__namaPertanyaan = namaPertanyaan
    def SetkodePertamyaan(self,kodePertanyaan):
        self.__kodePertanyaan = kodePertanyaan