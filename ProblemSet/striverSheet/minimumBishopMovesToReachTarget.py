source = eval(input("Enter the source position as a list [x, y]: "))
target = eval(input("Enter the target position as a list [x, y]: "))
#Color check
if (source[0] + source[1]) % 2 != (target[0] + target[1]) % 2:
    print("The target position is unreachable by the bishop.")
#Same diagonal check
if abs(source[0] - target[0]) == abs(source[1] - target[1]):
    print("The target position is reachable by the bishop in 1 move.")
else:
    #same color but not on the same diagonal
    print("The target position is reachable by the bishop in 2 moves.")