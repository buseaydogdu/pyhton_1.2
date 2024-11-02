import turtle as t
import random as r    #random rastgele bişeyler üretir
#randint içerisinde bir sayı olmalı.

# print(random.Random())
# print(random.randint(1,15))

t.speed()
renkler = ["blue","red","mor","al","purple"]

for b in range(9):
    t.color(r.choice(renkler))    #choice seçenek

    t.penup()

    t.goto(r.randint(-400,400),100)
    t.pendown()
    kenar = r.randint(-400,400)
    for a in range(4):
        t.forward(kenar)
        t.right(90)

input()    