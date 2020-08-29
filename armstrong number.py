sayi = (input("Lutfen pozitif bir tam sayi giriniz:"))
us = len(sayi)
sayac = 0
if not sayi.isdigit() :
    print(sayi, "It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif int(sayi) >= 0:
    for i in range(us):
        sayac += int(sayi[i]) ** us
    if sayac == int(sayi):
        print(sayi, "Is an Armstrong number.")
    else:
        print(sayi, "is not an Armstrong number.")