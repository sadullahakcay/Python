age = input("Are you a cigarette addict older than 75 years old?(Yes/No):")
age1 = age.capitalize()
chronic = input("Do you have a severe chronic disease?(Yes/No):")
chronic1 = chronic.capitalize()
immune = input("Is your immune system too weak?(Yes/No):")
immune1 = immune.capitalize()
if (age1 == "Yes") or (chronic1 == "Yes") or (immune1 == "Yes") :
    print("You are in risky group")
else:
    print("You are not in risky group")