stock = eval(input("Enter the prices: "))
maxProfit = 0
for i in range(len(stock)):
    for j in range(i+1, len(stock)):
        if stock[j] > stock[i]:
            maxProfit = max(maxProfit, stock[j] - stock[i])
print("The maximum profit that can be achieved is:", maxProfit)

#Optimal Approach
minPrice = float('inf')
maxProfit = 0
for price in stock:
    if price < minPrice:
        minPrice = price
    else:
        maxProfit = max(maxProfit, price - minPrice)
print("The maximum profit that can be achieved is:", maxProfit)