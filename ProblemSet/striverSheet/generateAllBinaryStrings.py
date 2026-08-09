n = int(input("Enter the number of bits: "))
result = []
for i in range(2**n):
    binary_string = bin(i)[2:].zfill(n)
    if '11' not in binary_string:
        result.append(binary_string)
print("All binary strings of length", n, "without consecutive 1s:")
print(result)
    
        