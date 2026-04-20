moves = input("Enter the string of moves: ")

l = moves.count('L')
r = moves.count('R')
s = moves.count('_')

max_distance = abs(r - l) + s

print("Maximum distance from origin:", max_distance)