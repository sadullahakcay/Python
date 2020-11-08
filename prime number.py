sayi = int(input("Lutfen bir tamsayi giriniz: "))
bolen_say = 0
for i in range(1, sayi+1) :
    if sayi % i == 0 :
        bolen_say += 1
if (sayi < 2) or (bolen_say > 2) :
    print(sayi, "is not a prime number")
else:
    print(sayi, "is a prime number")