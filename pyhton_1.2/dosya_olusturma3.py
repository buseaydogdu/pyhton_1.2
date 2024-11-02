# a=open(f"rehber1.txt","w") 
# a=open(f"rehber1.txt","r") 
# a.write("çarşamba")
# r=read (eğer mod belirtilmezse r olarak kabul edilir.)
# a=open(f"RehberCagir.py")

a=open(f"dosyalar.txt",encoding="utf8")
# Türkçe karakter desteği için.
print(a)
okunan = a.read()
print(okunan)
a.close()
import os
# os=operatin system = dosya silme
os.remove("dosyalar.txt")