for i in range(1, 101):
    if i % 15 == 0 :
        print("i".replace("i","FizzBuz"))
    elif i % 3 == 0 :
        print("i".replace("i","Fizz"))
    elif i % 5 == 0 :
        print("i".replace("i","Buz"))
    else :
        print(i)