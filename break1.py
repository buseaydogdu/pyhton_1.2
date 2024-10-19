for a in range(1,11):
    if a == 3 : continue   #continue bu turu atla geç.
    for b in range(1,11):
        print(a,"x",b,"=",a*b)
    print()   
    if a == 5 : break  #break gördüğü yerde bitiriyor.
