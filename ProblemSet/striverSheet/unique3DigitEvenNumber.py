digits = eval(input("Enter the digits: "))
answer = 0
freq = [0]*10

for d in digits:
    freq[d] += 1

for hundred in range(1,10):
    for ten in range(0,10):
        for unit in range(0,10,2):
            if freq[hundred]==0 or freq[ten]==0 or freq[unit]==0:
                continue
            if hundred==ten==unit and freq[hundred]<3:
                continue
            if hundred==ten and freq[hundred]<2:
                continue
            if hundred==unit and freq[hundred]<2:
                continue
            if ten==unit and freq[ten]<2:
                continue
            answer += 1
print("The number of unique 3-digit even numbers that can be formed is:", answer)
