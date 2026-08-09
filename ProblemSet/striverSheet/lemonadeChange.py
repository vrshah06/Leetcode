bills = eval(input("Enter a list of bills: "))
boolean = True
if bills[0] != 5:
    boolean = False
fives = 0
tens = 0
for bill in bills:
    if bill == 5:
        fives += 1
    elif bill == 10:
        if fives>0:
            fives -= 1
        else:
            boolean = False
            break
        tens += 1
    else:
        if fives>0 and tens>0:
            fives -= 1
            tens -= 1
        elif fives>=3:
            fives -= 3
        else:
            boolean = False
            break
print(boolean)