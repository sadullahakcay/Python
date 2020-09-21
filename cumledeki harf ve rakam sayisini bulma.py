cumle = input("bir cumle giriniz: ")
digit = leters = 0
for i in cumle:
    if i.isalpha():
        leters += 1
    elif i.isdigit():
        digit += 1
print("Digit:", digit)
print("Leters:", leters)