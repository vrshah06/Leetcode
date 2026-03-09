nums = eval(input("Enter binary numbers: "))

temp = []

for num in nums:
    temp.append(int(num,2))

m = max(temp)

for i in range(m+1):
    if i not in temp:
        print(bin(i)[2:])
        break
else:
    print(bin(m+1)[2:])


# nums = eval(input("Enter the numbers: "))
# temp=[]
# unique=[]
# for num in nums:
#     value = 0
#     for i in num:
#         value = value*2+int(i)
#     temp.append(value)
# m=max(temp)
# n=m+1
# binary=""
# for i in range(m):
#     if i in temp:
#         continue
#     else:
#         if i==0:
#             binary="0"
#         else:
#             while i>0:
#                 binary=str(i%2)+binary
#                 i//=2
#         unique.append(binary)
#     binary=""
# b=""
# if unique==[]:
#     if (n)==0:
#         b="0"
#     else:
#         while n>0:
#             b=str(n%2)+b
#             n//=2
# print(b)
    

    
        