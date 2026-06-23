num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
count = 0
for i in range(int(num1), int(num2)+1):
    num_str = str(i)
    for j in range(1, len(num_str)-1):
        if (num_str[j] > num_str[j-1] and num_str[j] > num_str[j+1]) or (num_str[j] < num_str[j-1] and num_str[j] < num_str[j+1]):
            count += 1
print(count)