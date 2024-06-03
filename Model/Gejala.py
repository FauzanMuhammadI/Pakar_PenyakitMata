class GejalaModel:
    def __init__(self,kodegejala,namagejala):
        self.__kodegejala = kodegejala
        self.__namagejala = namagejala
    def Getnamagejala(self):
        return self.__namagejala
    def Getkodegejala(self):
        return self.__kodegejala
    def Setnamagejala(self,namagejala):
        self.__namagejala = namagejala
    def Setkodegejala(self,kodegejala):
        self.__kodegejala = kodegejala