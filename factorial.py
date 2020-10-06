sayi = int(input("Bir sayi giriniz: "))
fac = 1
for i in range(1, sayi+1):
    fac *= i
print("{} sayisinin faktoriyeli : {} ".format(sayi, fac))