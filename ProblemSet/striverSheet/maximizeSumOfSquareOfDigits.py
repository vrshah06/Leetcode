num = int(input("Enter a number: "))
sum = int(input("Enter a sum: "))
if sum > 9*num:
    print("Not possible")
ans = []
for _ in range(num):
    digit = min(9, sum)
    ans.append(str(digit))
    sum -= digit
if sum== 0:
    print("The maximum number is:", ''.join(ans))
else:
    print("Not possible")