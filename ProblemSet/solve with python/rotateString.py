s = input("Enter the string: ")
goal = input("Enter the goal string: ")
temp = s
if len(s) != len(goal):
    print("False")
else:
    for i in range(len(s)):
        temp = temp[1:]+temp[0]
        if temp == goal:
            print("True")
            break
    else:
        print("False")
