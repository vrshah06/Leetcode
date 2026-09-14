weights = eval(input("Enter the weights of the items as a list: "))
values = eval(input("Enter the values of the items as a list: "))
capacity = int(input("Enter the capacity of the knapsack: "))
items = []
for i in range(len(weights)):
    ratio = values[i] / weights[i]
    items.append((ratio, weights[i], values[i]))
items.sort(reverse=True)
total_value = 0
for ratio, weight, value in items:
    if capacity >= weight:
        total_value += value
        capacity -= weight
    else:
        total_value += ratio * capacity
        capacity = 0
        break
print("The maximum value that can be obtained is:", total_value)