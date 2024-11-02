class Ogrenci():
    adi="--"
    ortalamasi=50

    def __init__(aa,xx,yy):
        aa.adi=xx
        aa.ortalamasi=yy
    
ogrenci1= Ogrenci("Buse AYDOĞDU",81)
ogrenci2= Ogrenci("Ebru GÜNDEŞŞ",91)   


print(ogrenci2)
print(ogrenci2.adi)
print(Ogrenci.adi) 
