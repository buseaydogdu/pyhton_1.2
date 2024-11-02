abc = "merhaba buse" # string (metin türü) bir değişken tanımladık

print ("merhaba".capitalize()) # İlk harf büyük
print("MERhAbA".lower()) # küçük harfe çevir
print("merhAba".upper()) # büyük harfe çevir
print(abc.swapcase()) # Büyük küçük harfleri değiştir.   swapcase = takas
print(abc.title()) # Kelimelerin ilk harflerini büyüt  title = başlık
print(abc.replace("h","u")) # “E” leri “a” yap       replace = yer değiştirmek 

print(abc.upper().replace("h","u")) # Önce büyük harfe çevir, sonra “E” leri “a” yap

print(abc.count("b")) # Metindeki bazı karakteler veya karakter gruplarının sayısı   count = saymak
print(abc.find("bus")) # “Dö” ifadesi kaçıncı indexte   find = bulmak
