def calculator(a, b, opr) :
    if opr == "+" :
        print(a + b)
    elif opr == "-" :
        print(a - b)
    elif opr == "*" :
        print(a * b)
    elif opr == "/" :
        print(a / b)
    else :
        print("enter valid arg")                

calculator(3, 5, "+")