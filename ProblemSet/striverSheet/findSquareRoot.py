num = int(input("Enter a number: "))
ans=0
for i in range(1,num+1):
    if i*i<=num:
        ans=i
    else:
        break
print(ans)

#Method 2
low = 1
high = num
while low<=high:
    mid = (low+high)//2
    if mid*mid<=num:
        ans=mid
        low=mid+1
    else:
        high=mid-1
print(ans)