class UserModel:
    def __init__(self,name,password):
        self.__name = name
        self.__password = password
    def Getname(self):
        return self.__name
    def Getpassword(self):
        return self.__password
    def Setname(self,name):
        self.__name = name
    def Setpassword(self,password):
        self.__password = password
