cost = eval(input("Enter the cost of the candies: "))
cost.sort()
total_cost = 0
i = len(cost) - 1
while i>=0:
    total_cost += cost[i]
    if i-1 >= 0:
        total_cost += cost[i-1]
    i -= 3
print("The minimum cost of buying the candies is: ", total_cost)