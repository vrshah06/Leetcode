num = input("enter the number: ")
half_length = len(num) // 2
first_half = num[:half_length]
second_half = num[half_length:]
q1 = first_half.count('?')
q2 = second_half.count('?')
if (q1+q2) % 2 != 0:
    print(True)
s1 = sum(int(digit) for digit in first_half if digit != '?')
s2 = sum(int(digit) for digit in second_half if digit != '?')
if 2 * s1 + 9 * q1 != 2 * s2 + 9 * q2:
    print(True)
else:
    print(False)