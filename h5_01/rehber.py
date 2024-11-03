def rehber_ekle():
    dosya= open("rehber.txt","a")
    print("\n\n Rehbere eklenecek bilgileri giriniz:")
    ad  = input("Ad : ")
    tel = input("Tel : ")
    dosya.write(f"{ad}#{tel}\n")
    print("\n\n Rehberdekiler (yeni şekli):")
    rehber_listele()
def rehber_listele():
    print("\n\n Rehberiniz:")
    dosya = open("rehber.txt")
    okunan = dosya.readlines()
    # print(okunan)
    # for a in okunan:
    for sira,a in enumerate(okunan):
        b=a.split("#")
        print(f"{sira+1}-{b[0]},\t Telefonu: {b[1]}")
    dosya.close()

def rehber_sil():
    print("Mevcut kayıtlar")
    rehber_listele()
    silinecek=input("Hangi kayıt silinecek(numarasını girin)":)
    dosya=open("rehber.txt")
    okunan=dosya.readlines()
    for s,a in enumerate(okunan):
        print(s,a)
    # dosya.close()
    # dosya=open("rehber.txt","w")
   
    # for sira,a in enumerate(okunan):
    #     if sira != silinecek: dosya.write(a)

    # dosya.close()


def rehber_duzelt():
    pass        

def anamenu():
   print("╔═════════════════════╗")
   print("║  REHBER UYGULAMASI  ║")
   print("║   --- --- ---  ---  ║")
   print("║ 1-Rehber ekle       ║")
   print("║ 2-Kişi listesi      ║")
   print("║ 3-Kişi düzenle      ║")
   print("║ 4-Kişi silme        ║")
   print("║ 5-Çıkış             ║")
   print("║                     ║")
   print("║ Seçiminiz nedir?    ║")
   print("╚═════════════════════╝")

   secim=input()

   if secim=="1": rehber_ekle(); anamenu()
   if secim=="2": rehber_listesi(); anamenu()
   if secim=="3": rehber_duzelt(); anamenu()
   if secim=="4": rehber_sil(); anamenu()
   if secim=="5": rehber_ekle(); anamenu()

anamenu()

