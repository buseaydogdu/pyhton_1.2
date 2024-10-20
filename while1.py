import random as rn
renkler =  ["blue","red","tomato","al","purple"]
for a in renkler: print(a)

renk = ""
while renk != "red":    #!= eşit değil demek
    renk = rn.choice(renkler)
    print(renk)

