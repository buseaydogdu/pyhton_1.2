a="Erdinnç DÖNMEZ"

for b in range(len(a)):
    print(a[:b],end=""+" "*(len(a)-b)+"|"+" "*(len(a)-b)+a[-1:len(a)-b:-1])
    print()