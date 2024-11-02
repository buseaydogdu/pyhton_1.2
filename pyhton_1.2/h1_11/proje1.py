print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
print("║                     ║")
print("║  1-Toplama          ║")
print("║  2-Çıkarma          ║")
print("║  3-Çarpma           ║")
print("║  4-Bölme            ║")
print("║  5-Karekök          ║")
print("║  6-Küp              ║")
print("║  7-Logaritma        ║")
print("║  8-Yüzde            ║")
print("║  9-                 ║")
print("║  10-                ║")
print("║                     ║")
print("║  Seçimiz nedir?     ║")
print("╚═════════════════════╝")


secim=input()

print(secim,"seçtiniz.")
if secim == "1" :
    print("1 seçtiniz, toplama yapılacak.")
if secim == "2" :
    print("2 seçtiniz, çıkarma yapılacak.")
if secim == "3" :
    print("3 seçtiniz, çarpma yapılacak.") 
if secim == "1,2" :
    print("1,2 seçtiniz, toplama ve çıkarma yapılacak.")

#Alınacaklar:
#   -makarna
#   -soğan      (if(eğer) yapısına benzer.)
