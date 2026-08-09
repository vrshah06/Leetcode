start = int(input("Enter the start number: "))
goal = int(input("Enter the goal number: "))
xor = start ^ goal
count = 0
for i in range(32):
    # Update count if the 
    # rightmost bit is set
    count+= (xor & 1)

    # Shift the number every
    # time by 1 place
    xor >>=1
print(count)

