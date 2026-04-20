sum=0
d = int(input("Enter the days: "))
m=1
sun=7
s=d//7
for i in range(s):
    for j in range(1,sun+1):
        sum+=j
    m+=1
    sun+=1
for k in range(d%7):
    sum=sum+m
    m+=1
print(sum)

# class Solution:
#     def totalMoney(self, n: int) -> int:
#         total = 0
#         full_weeks = n // 7
#         remaining_days = n % 7

#         # Add full weeks
#         for week in range(full_weeks):
#             total += 7 * (week + 1) + 21  # 21 = 1+2+3+4+5+6+7 - 7*(1)

#         # Add remaining days
#         start = full_weeks + 1
#         for day in range(remaining_days):
#             total += start + day

#         return total
