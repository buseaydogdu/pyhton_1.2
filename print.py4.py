m1="şehirler"
m2="ankara"
m3="izmir"
m4=f"iller {m3} -- {m2}"
m5=f"{m1} {m4} {m2}"
m6="iller {m2}"
m7="şehirler: {}, {}".format(m2,m3)
m8="şehirler:  %s,  %s" %(m2,m3)
print(m4)
print(m5)
print(m6)

#pythonda string formatlama (metin şekillendirme)
print(f"şehirler: {m2}, {m3}")
print("şehirler: {}, {}".format(m2,m3))
print("şehirler:  %s,  %s" %(m2,m3))

print(m6)
print(m7)
