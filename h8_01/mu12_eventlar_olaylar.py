from PyQt6.QtWidgets import*

class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()

        def xxx():
            mesaj = "Giriş düğmesine tıklandı"
            print(mesaj)
            dlg= QMessageBox(self)
            dlg.setWindowTitle("Dikkat")
            dlg.setText(mesaj)
            dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            dlg.setIcon(QMessageBox.Icon.Question)
            dlg.exec()

        
        def yyy():
            print("Vazgeç düğmesine tıklandı.")
            aaa= QMessageBox(self)
            aaa.setWindowTitle("Aman Dikkat")
            aaa.setText("Vazgeç düğmesine tıkladınız.")
            aaa.exec()


        di6= QVBoxLayout()
        yatayicerik = QHBoxLayout()
        
        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Kullanıcı adı"))
        dikeyicerik3.addWidget(QLabel("Şifresi"))

        dikeyicerik4 = QVBoxLayout()
        self.kullanici_adi=QLineEdit()
        dikeyicerik4.addWidget(self.kullanici_adi)

        self.sifre=QLineEdit()
        dikeyicerik4.addWidget(self.sifre)
    

        yi5= QHBoxLayout()
        dugme1= QPushButton("Giriş yap")
        yi5.addWidget(dugme1)
        dugme1.clicked.connect(xxx)

        dugme2=QPushButton("Vazgeç")
        

        yi5.addWidget(dugme2)
        dugme2.clicked.connect(yyy)
        

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)
        pencere= QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

aa=QApplication([])        
pencere=GirisEkrani()
pencere.show()
aa.exec()


                          