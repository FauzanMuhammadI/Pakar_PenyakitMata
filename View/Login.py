import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
from Controller.UserController import UserController
from Model.User import UserModel
from View.Forward import Forward


# Definisi kelas utama aplikasi
class showimage(QtWidgets.QMainWindow):
    def __init__(self):
        super(showimage, self).__init__()
        loadUi('Login_view.ui', self)
        self.Login_btn.clicked.connect(self.Login)

        # Menghubungkan event klik pada label_3 dengan fungsi Register1
        self.label_3.mousePressEvent = self.Register1
        self.nama = None

    # Fungsi untuk membuka form registrasi
    def Register1(self, event):
        from View.Register import Register
        try:
            self.register = Register()
            self.register.show()
            self.hide()
        except Exception as e:
            print(e)

    # Fungsi untuk melakukan login
    def Login(self):
        username = self.Username_edt.text()
        password = self.Password_edt.text()

        usc = UserController()
        User = UserModel(username, password)
        hasil = usc.Logic_Login(User)

        if hasil == -1:
            self.show_popup("Username Atau Password Salah")

        else:
            try:
                self.Forward = Forward()
                self.Forward.show()
                self.Forward.Kode_edt.setText(username)
                self.Forward.Kode_edt_2.setText("USR-00" + str(hasil))
                self.hide()
            except Exception as e:
                print(e)

    # Fungsi untuk menampilkan popup pesan error
    def show_popup(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Login Error")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


# Menjalankan aplikasi
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = showimage()
    window.setWindowTitle('Sistem Pakar')
    window.show()
    sys.exit(app.exec_())
