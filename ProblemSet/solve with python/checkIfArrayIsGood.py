nums = eval(input("Enter the array: "))
l = len(nums)-1
seen = set()
flag = False
for num in nums:
    if num>l:
        print("False")
        break
    if num in seen:
        if num<l or flag:
            print("False")
            break
        flag = True
    seen.add(num)
print("True")