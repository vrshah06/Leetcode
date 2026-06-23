gain = eval(input("Enter the gain values as a list: "))
altitude = 0
highest_altitude = 0
for g in gain:
    altitude += g
    if altitude > highest_altitude:
        highest_altitude = altitude
print("The highest altitude reached is:", highest_altitude)