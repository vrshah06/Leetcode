ratings = eval(input("Enter the ratings of the children as a list: "))
candies = [1] * len(ratings)  # Initialize the number of candies for each child to 1
update = True  # Flag to check if any updates were made in the last iteration
while update:
    update = False
    for i in range(len(ratings)):
        if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
            candies[i] = candies[i - 1] + 1
            update = True
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1
            update = True
print("Minimum number of candies needed:", sum(candies))