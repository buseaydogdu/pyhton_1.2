def listele(self):
    print("Listele düğmesine basıldı")
    import mysql.connector
    try:

        vts=mysql.connector.connect(host="localhost",user="root",password="1234",database="deneme1"
        ); print("Bağlantı tamam:")
        secilen = vts.cursor()                            
        alinan_liste= secilen.execute("select * from ogrenciler")
        xxx=secilen.fetchall()
        for a in xxx:
            print(a)
            # self.labelListe.getText
            self.labelListe.setText(f"{self.labelListe.text()}\n{a[0]},{a[4]}")