ogrenciler = ["sude akyol","rahime kara"]
ortalamalar = [79,89]

ogrenciOrtalamalari = {
    "ogrenci1":{"adi":"sude akyoll","ortalamalasi":80 },
    "ogrenci2":{"adi":"rahime karaa","ortalamalasi":90 },
    }
    
    
aranacak=input("hangi öğrenci bilgileri?")
if aranacak != "":
    print(ogrenciOrtalamalari,{aranacak}["adi"])
else: 
    print("boş geçme")         


# print(ogrenciOrtalamalari["adi1"],ogrenciortalamalari["ortalamasi1"])