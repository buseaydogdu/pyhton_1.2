meyveler= ["elma","muz","nar","dut"]
çorbalar=["tarhana","mercimek","yayla"]

print(meyveler)
print(*meyveler)
print(*meyveler, sep=",")
print(*meyveler, sep="\t")
print(*çorbalar, sep="\n")


print("van","muş","çan","bor")
print("van","muş","çan","bor",sep=" ")
print("van","muş","çan","bor",sep="-")

print("van","muş","çan","bor", end="")
print("van","muş","çan","bor",sep="-",end="")
print("şehirler")

print("van","muş","çan","bor")
#end parametresi print ile yazdıktan sonra ne yapılacağını belirtir.
#sep (seperate) parametresi print ile birden çok ifade arasında neler olacağını ifade eder.
