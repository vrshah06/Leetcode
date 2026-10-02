num = int(input("Enter a number: "))
count = 0
result = []
for i in range(2, num + 1):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        count += 1
        result.append(i)
print(f"Number of primes in the range 2 to {num} is: {count}")
print(f"Primes in the range 2 to {num} are: {result}")