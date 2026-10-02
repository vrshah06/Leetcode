prices = eval(input("Enter the prices of the items as a list: "))
discounts = eval(input("Enter the discounts for each item as a list: "))
total_price = 0
prices.sort(reverse=True)  # Sort prices in descending order
discounts.sort(reverse=True)  # Sort discounts in descending order
for i in range(min(len(prices), len(discounts))):
    total_price += prices[i] * (100 - discounts[i]) / 100
for i in range(len(discounts), len(prices)):
    total_price += prices[i]
print("Minimum total price after applying discounts:", total_price)