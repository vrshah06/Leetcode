l= int(input("Enter the value of L: "))
r= int(input("Enter the value of R: "))
for i in range(l,r+1):
    xor=0
    for j in range(l,i+1):
        xor^=j
    print("XOR of numbers from",l,"to",i,"is:",xor)