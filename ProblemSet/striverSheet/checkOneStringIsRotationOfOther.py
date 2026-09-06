s = input("Enter the first string: ")
goal = input("Enter the target string: ")
if len(s) != len(goal):
    print("The strings are not rotations of each other.")
else:
    #left shift the string and check if it matches the target string
    for i in range(len(s)):
        s = s[1:] + s[0]
        if s == goal:
            print("The strings are rotations of each other.")
            break
    else:
        print("The strings are not rotations of each other.")