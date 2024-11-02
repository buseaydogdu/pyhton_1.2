class Ogrenci:
    adi="--"
    ortalamasi=50

print(Ogrenci)
print(Ogrenci.adi)
print(Ogrenci.ortalamasi)

ogrenci1= Ogrenci()
print(Ogrenci)
print(Ogrenci.adi)
print(Ogrenci.ortalamasi)

ogrenci1.adi="nurdan sarı"
print(ogrenci1.adi)

ogrenci2 = Ogrenci
print(ogrenci2.adi)
print(Ogrenci.adi)

ogrenci2.adi = "ömer aybak"
print(ogrenci2.adi)
print(ogrenci1.adi)
