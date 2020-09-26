isim = input("Adinizi giriniz: ")
kilo = int(input("Kilonuzu kg olarak giriniz: "))
boy = float(input("Boyunuzu metre olarak giriniz: "))
endeks = kilo / (boy**2) 
endeks = round(endeks, 2)
if 0 < endeks <= 18.4 :
    print("{} kilo endeksin {} ve zayifsin.".format(isim, endeks))
elif 18.4 < endeks <= 24.9 :
    print("{} kilo endeksin {} ve normalsin.".format(isim, endeks))
elif 24.9 < endeks <= 29.9 :
    print("{} kilo endeksin {} ve kilolusun.".format(isim, endeks))
elif 29.9 < endeks <= 46 :
    print("{} kilo endeksin {} ve obezsin.".format(isim, endeks))
else :
    print("Bilgilerinizi kontrol ediniz.")    