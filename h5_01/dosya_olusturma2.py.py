# a=open(f"dosyalar","a")
# w=write modunda öncekiler silinir.

a=open(f"dosyalar","a")
#  a=append ile açıldığında öncekilere eklenir.
for b in range(10):
    # a.write(str(b))
    a.write(f"{str(b)}\n") 

