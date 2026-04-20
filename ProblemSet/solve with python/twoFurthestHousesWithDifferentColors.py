colors = eval(input("Enter the colors: "))
maxDistance = 0
for color in range(len(colors)):
    for otherColor in range(color + 1, len(colors)):
        if colors[color] != colors[otherColor]:
            distance = abs(color - otherColor)
            if distance > maxDistance:
                maxDistance = distance
print("The maximum distance between two houses with different colors is", maxDistance)
