from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from Controller.UserController import UserController
from Model.User import UserModel

class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super(Register, self).__init__()
        loadUi('Register_view.ui', self)
        self.Register_btn.clicked.connect(self.Register)
        self.label_3.mousePressEvent = self.Login
        self.nama = None

    def Register(self):
        username = self.Username_edt.text()
        password = self.Password_edt.text()
        usc = UserController()
        User = UserModel(username, password)

        if username == "" or password  == "":
            self.Login_lb.setText("Username atau Password tidak pleh kosong")
            self.Login_lb.setText("Usernaem sudah di pakai")
        else:
            hasil = usc.Logic_Register(User)
            if hasil == -1:
                self.Login_lb.setText("Usernaem sudah di pakai")
            else:
                self.Login_lb.setText("Akun berhasil di buat")

    def Login(self,event):
        from View.Login import showimage

        self.login = showimage()
        self.login.show()
        self.hide()




