n = range(1, 101)
prime_numbers = []
for j in range(1, 101) :
    bolen_say = 0
    for i in range(1, j+1) :
        if j % i == 0 :
            bolen_say += 1
    if (j >= 2) and (bolen_say <= 2) :
        prime_numbers.append(j)
print(prime_numbers)