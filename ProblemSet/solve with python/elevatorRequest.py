n = int(input("Number of floors: "))
requests = eval(input("Enter a list of requests: "))
total_time = 0
current_floor = 0
for request in requests:
    total_time += abs(request - current_floor)
    current_floor = request
print(total_time)