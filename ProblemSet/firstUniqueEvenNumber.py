nums = eval(input("Enter the numbers: "))
temp=[]
for i in nums:
    if i%2==0 and nums.count(i)==1:
        print(i)
        break
else:
    print(-1)
        
        