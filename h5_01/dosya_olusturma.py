# open("deneme","w")
# (dosya adı,yapacagı işlem)
# ctrl+d istediğim aynılarını seçiyor


# open("modul1","w")
import os 
import time
# ka=input("modul1:")
# os.mkdir(ka)


# for a in range(10):
#     open("virus.bat","w") # w modu dosyanın içindekileri siler öncekileri.

# for a in range(10):
    # print(f"virus{a}.bat")
    # time.sleep(1)
    # # open(f"virus{a}.bat,"a")
    # os.remove(f"virus{a}.bat,"a")

# for a in range(10):
#     os.remove(f"virus{a}.bat")

# open("arçelik_faturaları,"r")
# open("arçelik_faturaları,"r").read()
# okunan=open("arçelik-faturaları","r").read

# print(okunan)

dosya=open("arçelik_faturaları","r+")
okunan=dosya.read()
print(okunan)

dosya.write("\n2024-1103 12500TL")

okunan=dosya.read()
print(okunan)