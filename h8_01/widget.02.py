import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
duvar= QMainWindow()

tablo1 =QVBoxLayout()

tablo1.addWidget(QLabel("Kullanıcı adı:"))
tablo1.addWidget(QLineEdit())

tablo1.addWidget(QLabel("şifre:"))
tablo1.addWidget(QLineEdit())

tablo1.addWidget(QPushButton("Giriş"))
tablo1.addWidget(QCheckBox("Beni hatırla"))

ailefotografi = QWidget()
ailefotografi.setLayout(tablo1)

duvar.setCentralWidget(ailefotografi)

duvar.show()
app.exec()