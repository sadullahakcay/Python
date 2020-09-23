cumle = input("Bir cumle giriniz:").lower()
sesli = sessiz = 0
for i in cumle:
    if i in set("euioa"):
        sesli += 1
    elif i in set("qwrtzpsdfghjklyxcvbnm"):
        sessiz += 1
print(f"Girdiginiz cumle icinde {sesli} sesli harf, {sessiz} sessiz harf var.")            