import math
sides = eval(input("Enter the sides of the triangle: "))
sides.sort()
if sides[0] + sides[1] > sides[2]:
    cosineA = (sides[1]**2 + sides[2]**2 - sides[0]**2) / (2 * sides[1] * sides[2])
    cosineB = (sides[0]**2 + sides[2]**2 - sides[1]**2) / (2 * sides[0] * sides[2])
    cosineC = (sides[0]**2 + sides[1]**2 - sides[2]**2) / (2 * sides[0] * sides[1])
    angles.append(math.degrees(math.acos(cosineA)))
    angles.append(math.degrees(math.acos(cosineB)))
    angles.append(math.degrees(math.acos(cosineC)))
    print("The angles of the triangle are", math.degrees(math.acos(cosineA)), "degrees", math.degrees(math.acos(cosineB)), "degrees and", math.degrees(math.acos(cosineC)), "degrees")
else:
    print([])
