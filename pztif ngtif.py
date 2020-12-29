sayi = input("sayı gir")
if sayi.lstrip("-").isdigit:
    if int(sayi)>0:
        print("sayı poziyif")
    elif int(sayi)<0:
        print("sayı negatif")
    else:
        print("sayı sıfır")