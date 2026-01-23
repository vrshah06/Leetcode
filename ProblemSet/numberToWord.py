num = int(input("Enter the number: "))
data = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
    14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
    18: "Eighteen", 19: "Nineteen", 20: "Twenty",
    30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty",
    70: "Seventy", 80: "Eighty", 90: "Ninety"}
if num <= 20:
    print(data[num])
elif num < 100:
    if num % 10 == 0:
        print(data[num])
    else:
        print(data[num - num % 10] + " " + data[num % 10])
elif num < 1000:
    if num % 100 == 0:
        print(data[num // 100] + " Hundred")
    else:
        remainder = num % 100
        if remainder <= 20:
            print(data[num // 100] + " Hundred " + data[remainder])
        else:
            if remainder % 10 == 0:
                print(data[num // 100] + " Hundred " + data[remainder])
            else:
                print(data[num // 100] + " Hundred " + data[remainder - remainder % 10] + " " + data[remainder % 10])
    
    