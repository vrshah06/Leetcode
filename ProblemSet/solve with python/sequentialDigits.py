low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
result = []
for i in range(low,high+1):
    str_i = str(i)
    if len(str_i) > 1:
        is_sequential = False
        for j in range(len(str_i)-1):
            if int(str_i[j+1]) - int(str_i[j]) == 1:
                is_sequential = True
            else:
                is_sequential = False
                break
    if is_sequential:
        result.append(i)
result = list(set(result))
result.sort()
print("Sequential digits in the range are:", result)


# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#         result = []
#         for i in range(1,10):
#             num=i
#             for j in range(i+1,10):
#                 num = num*10 + j
#                 if low<=num<=high:
#                     result.append(num)
#         result.sort()
#         return result
        