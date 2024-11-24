# veritabanı sistemine bağlanmak için gerekli kodlar.
import mysql.connector

try:
  vts = mysql.connector.connect(
    host="localhost", # Veritabanı sistemi adı (instance).
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="ots"
  )
  print("Bağlantı tamam:")


  try:
    secilen = vts.cursor()
    secilen.execute("CREATE TABLE ogrenciler (ad VARCHAR(50), telefon VARCHAR(30))")
    secilen.execute("CREATE TABLE veliler (ad VARCHAR(50), telefon VARCHAR(30))")
    print("Tablo oluşturuldu.")

  except mysql.connector.Error as hata:
    print(f"Veri tabanı oluşturulamadı.Hata : {hata}")

except:
  print("Veri tabanına bağlanırken bir hata oluştu.")
# veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
